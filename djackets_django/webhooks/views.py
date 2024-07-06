from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from order.models import Order
from django.shortcuts import get_object_or_404

@method_decorator(csrf_exempt, name='dispatch')
class WebhookReceiver(APIView):
    def post(self, request, *args, **kwargs):
        event = request.data
        event_type = event.get('type')
        order_id = event.get('data', {}).get('metadata', {}).get('order_id')

        if order_id:
            order = get_object_or_404(Order, id=order_id)
            if event_type == 'payment_approved':
                order.status = 'approved'
            elif event_type == 'payment_declined':
                order.status = 'declined'
            elif event_type == 'payment_captured':
                order.status = 'captured'
            elif event_type == 'payment_refunded':
                order.status = 'refunded'
            elif event_type == 'payment_voided':
                order.status = 'voided'
            else:
                # Handle other event types if necessary
                pass

            order.save()

        return Response({'status': 'success'}, status=status.HTTP_200_O)