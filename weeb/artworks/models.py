import uuid

from django.db import models
from users.models import User


class Artwork(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_published'
    )
    title = models.CharField(max_length=128, null=False, blank=False)
    description = models.CharField(max_length=1024, null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

    file = models.ForeignKey(
        'ImageFile', on_delete=models.CASCADE, null=False, blank=False
    )
    tags = models.ManyToManyField('Tag', related_name='artwork_tags')

    def __str__(self):
        return str(self.id)


class Tag(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='user_created'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ImageFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uploaded_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_uploaded'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
