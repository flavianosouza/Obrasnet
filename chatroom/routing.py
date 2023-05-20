from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:expert_id>/<str:user_id>/', consumers.ChatConsume.as_asgi())
]