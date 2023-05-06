from django.contrib import admin

from . import models

admin.site.register(models.Artwork)
admin.site.register(models.FavoriteArtwork)
admin.site.register(models.ImageFile)
admin.site.register(models.Tag)
