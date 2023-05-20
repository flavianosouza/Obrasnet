from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:expert_id>/<user_id>/', consumers.ChatConsume.as_asgi())
]