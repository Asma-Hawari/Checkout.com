import stripe 
import requests
from django.conf import  settings 
from django.http import Http404
from django.shortcuts import render

from rest_framework import permissions , authentication , status
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product , Order

from .serializers import OrderSerializer , MyOrderSerializer

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serlizer = OrderSerializer(data = request.data)
    if serlizer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serlizer.validated_data['items'])
        try:
            charge = stripe.Charge.create(
                amount = int(paid_amount * 100),
                currency='USD',
                description='paid amount from django',
                source=serlizer.validated_data['stripe_token']
            )

            serlizer.save(user=request.user , paid_amount = paid_amount)
            return Response(serlizer.data, status=status.HTTP_201_CREATED)
        except  stripe.error.StripeError as e:
            print(str(e))  
            return Response({"error"+ str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        print(serlizer.errors)     
        return Response(serlizer.data, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def cko(request):
    serlizer = OrderSerializer(data = request.data)
    if serlizer.is_valid():
        cko_api_key = settings.CKO_SECRET_KEY
        processing_channel_id = settings.CKO_CHANNEL_ID
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serlizer.validated_data['items'])
        try:
            response = requests.post(
                'https://api.sandbox.checkout.com/payments',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {cko_api_key}',
                },
                json={
                    "source": {
                        "type": "token",
                        "token": serlizer.validated_data['cko_token']  # Assuming the token is the same as Stripe token
                    },
                    "amount": int(paid_amount * 100),
                    "currency": "USD",
                    "payment_type": "Regular",
                    "processing_channel_id": processing_channel_id
                }
            )

            if response.status_code == 201:
                serlizer.save(user=request.user, paid_amount=paid_amount)
                return Response(serlizer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(response.json(), status=response.status_code)
        except requests.RequestException as e:
            print(str(e))
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        print(serlizer.errors)     
        return Response(serlizer.data, status=status.HTTP_400_BAD_REQUEST)


class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        print(request.user)  # Debug: Print the user to check if it's authenticated
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        orders = Order.objects.filter(user=request.user)
        print(orders)
        serializer = MyOrderSerializer(orders, many=True)
        print(serializer.data)
        return Response(serializer.data)







