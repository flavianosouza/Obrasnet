from django.db import models
from django.contrib.auth.models import User
from core.models import Expert

# Create your models here.

class Chatroom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    room_type = models.BooleanField(default=0)                      # 0: user chat, 1: expert chat
    description = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField(default=0)                          # 0: closed, 1: open
    password = models.CharField(max_length=255, default='111')

class ExpertChat(models.Model):
    expert = models.ForeignKey(
        Expert,
        on_delete=models.CASCADE
    )
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    send_type = models.BooleanField(default=0)  # 0: expert->client, 1: client->expert
    room = models.ForeignKey(
        'Chatroom',
        on_delete=models.CASCADE,
        null=True
    )
    message = models.TextField(null=True)
    type = models.SmallIntegerField(default=0)
    
    send_time = models.DateTimeField(auto_now_add=True)
    receive_time = models.DateTimeField(null=True)

class UserChat(models.Model):
    user1 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chat_user1'
    )
    user2 = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chat_user2'
    )

    room = models.ForeignKey(
        'Chatroom',
        on_delete=models.CASCADE,
        null=True
    )
    message = models.TextField(null=True)
    type = models.SmallIntegerField(default=0)
    
    send_time = models.DateTimeField(auto_now_add=True)
    receive_time = models.DateTimeField(null=True)