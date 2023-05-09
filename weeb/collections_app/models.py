import uuid

from artworks.models import Artwork
from django.db import models
from users.models import User


def uploaded_collection_covers_directory_path(instance, filename):
    file_extension = filename.split('.')[-1]
    return f'collection_covers/{instance.id}.{file_extension}'


class Collection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='collections'
    )
    name = models.CharField(max_length=128, null=False, blank=False)
    description = models.CharField(max_length=1024, null=True, blank=True)
    cover_image = models.ImageField(
        upload_to=uploaded_collection_covers_directory_path, null=False, blank=False
    )
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class CollectionArtwork(models.Model):
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name='artworks'
    )
    artwork = models.ForeignKey(
        Artwork, on_delete=models.CASCADE, related_name='collections_with_art'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['collection', 'artwork'], name='unique_collection_artwork'
            )
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.artwork.title} in {self.collection.name}'
