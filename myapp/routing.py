from django.urls import path
from .consumers import LangflowConsumer

websocket_urlpatterns = [
    path('ws/langflow/', LangflowConsumer.as_asgi()),
]
