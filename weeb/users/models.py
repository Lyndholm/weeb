import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=32, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    created_at = models.DateTimeField('Registration date', auto_now_add=True)


def uploaded_avatars_directory_path(instance, filename):
    file_extension = filename.split('.')[-1]
    return f'uploads/{instance.pk}.{file_extension}'


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, editable=False
    )
    nickname = models.CharField(max_length=32, blank=False, null=False)
    biography = models.CharField(max_length=256, blank=True, null=True)
    avatar = models.ImageField(
        upload_to=uploaded_avatars_directory_path,
        null=True,
        default='avatar-default.svg',
    )

    def __str__(self):
        return self.user.username
