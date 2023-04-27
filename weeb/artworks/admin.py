from django.contrib import admin

from .models import Artwork, ImageFile, Tag

admin.site.register(Artwork)
admin.site.register(ImageFile)
admin.site.register(Tag)
