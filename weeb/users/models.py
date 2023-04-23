import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=32, unique=True, editable=False, blank=False)
    created_at = models.DateTimeField('Registration date', auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, editable=False)
    nickname = models.CharField(max_length=32, blank=False, null=False)

    def __str__(self):
        return self.user.username
