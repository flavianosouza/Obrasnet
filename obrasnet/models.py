from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
        unique=True
    )
    desciption = models.CharField(
        max_length=255,
        null=True
    )
    sheetname = models.CharField(
        max_length=100,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Material(models.Model):
    title = models.CharField(
        max_length=255,
        db_index=True
    )
    image = models.TextField(
        null=True
    )
    # specification = ListCharField(
    #     base_field=models.CharField(max_length=200),
    #     size=100,
    #     max_length=(100 * 200),
    #     null=True
    # )
    specification = models.TextField(
        null=True
    )

    ref = models.CharField(
        max_length=30, 
        db_index=True,
        null=True
    )

    price = models.TextField(
        null=True
    )

    description = models.TextField(
        null=True
    )

    advantage = models.TextField(
        max_length=255,
        null=True
    )

    documentation = models.TextField(
        null=True
    )

    features = models.TextField(
        null=True
    )

    url = models.URLField()

    state = models.BooleanField(
        default = True
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        default = 1
    )

    created_at = models.DateTimeField(auto_now_add = True, null=True)

    def __str__(self):
        return self.title, self.image, self.description, self.url

class Design(models.Model):
    title = models.CharField(max_length=255)
    squere = models.FloatField()

    def __str__(self):
        return self.title
    
class Expert(models.Model):
    expert = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=150)
    use_state = models.BooleanField(default=0)

class ExpertChat(models.Model):
    expert = models.ForeignKey(
        'Expert',
        on_delete=models.CASCADE
    )
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    send_type = models.BooleanField(default=0)  # 0: expert->client, 1: client->expert
    room_name = models.CharField(max_length=100, db_index=True)
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

    send_type = models.BooleanField(default=0)  # 0: user1->user2, 1: user2->user1
    room_name = models.CharField(max_length=100, db_index=True)
    message = models.TextField(null=True)
    type = models.SmallIntegerField(default=0)
    
    send_time = models.DateTimeField(auto_now_add=True)
    receive_time = models.DateTimeField(null=True)