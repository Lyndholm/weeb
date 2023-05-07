# Generated by Django 4.2 on 2023-05-07 10:48

import artworks.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artworks', '0007_alter_favoriteartwork_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('cover_image', models.ImageField(upload_to=artworks.models.uploaded_images_directory_path)),
                ('is_public', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CollectionArtwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections_with_art', to='artworks.artwork')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artworks', to='collections_app.collection')),
            ],
        ),
        migrations.AddConstraint(
            model_name='collectionartwork',
            constraint=models.UniqueConstraint(fields=('collection', 'artwork'), name='unique_collection_artwork'),
        ),
    ]