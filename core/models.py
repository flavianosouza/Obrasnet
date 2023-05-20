from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expert(models.Model):
    expert = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        unique=True
    )

    name = models.CharField(max_length=150, db_index=True)
    image = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=50, db_index=True)
    description = models.TextField(null=True)
    use_state = models.BooleanField(default=1)