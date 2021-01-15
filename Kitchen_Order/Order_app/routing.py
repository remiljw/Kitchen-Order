from django.urls import path
from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/orders/', WSConsumer.as_asgi())
]