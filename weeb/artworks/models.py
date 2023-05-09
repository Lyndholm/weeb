import uuid

from django.db import models
from users.models import User


def uploaded_artfiles_directory_path(instance, filename):
    file_extension = filename.split('.')[-1]
    return f'artworks/{instance.id}.{file_extension}'


class Artwork(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artworks')
    title = models.CharField(max_length=128, null=False, blank=False)
    description = models.CharField(max_length=1024, null=True, blank=True)
    source = models.CharField(max_length=256, null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

    file = models.ForeignKey(
        'ImageFile', on_delete=models.CASCADE, null=False, blank=False
    )
    tags = models.ManyToManyField('Tag', related_name='artworks', blank=True)

    class Meta:
        ordering = ['-published_at']

    def is_favored_by_user(self, user):
        return self.favored_by.filter(user=user).exists()

    def __str__(self):
        return str(self.id)


class FavoriteArtwork(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorite_artworks'
    )
    artwork = models.ForeignKey(
        Artwork, on_delete=models.CASCADE, related_name='favored_by'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'artwork'], name='unique_favorite')
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.artwork.title} favored by {self.user.username}'


class Tag(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='created_tags'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ImageFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.ImageField(
        upload_to=uploaded_artfiles_directory_path, null=False, blank=False
    )
    uploaded_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='uploaded_image_files'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
