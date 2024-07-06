from django.urls import path,include
from order import views


urlpatterns = [
    path('checkout/', views.checkout),
    path('cko/', views.cko),
    path('orders/',views.OrdersList.as_view())
]