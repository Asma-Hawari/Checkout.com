from django.urls import path
from .views import WebhookReceiver


urlpatterns = [
    path('webhook-receiver/', WebhookReceiver.as_view(), name='webhook-receiver'),
]