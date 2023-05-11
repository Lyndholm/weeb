import io

from django.core.files.storage import default_storage
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

from .models import ImageFile


# TODO: Celery task for image optimizing?
@receiver(post_save, sender=ImageFile)
def optimize_image_file(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.file.name.split('.')[-1].lower() == 'gif':
        return

    original_image = Image.open(instance.file)
    optimized_image = original_image.copy().convert('RGB')
    optimized_image_file = io.BytesIO()

    quality = 75
    optimized_image.save(
        optimized_image_file, format='JPEG', optimize=True, quality=quality
    )

    original_image_path = instance.file.name.split('.')[0].rstrip('.')
    optimized_image_path = f'{original_image_path}_compressed.jpg'

    default_storage.save(optimized_image_path, optimized_image_file)

    instance.compressed_file.name = optimized_image_path
    instance.save()
