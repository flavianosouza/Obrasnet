from django.contrib.auth import views as auth_views
from django.urls import path

from chatroom.views import *

urlpatterns = [
    path("expert_list", expert_list, name="expert_list"),
    path("expert_chat/<expert_id>/<user_id>", expert_chat, name="expert_chat"),
    path("user_chat", user_chat, name="user_chat"),
]