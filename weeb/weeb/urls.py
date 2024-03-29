import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin_route = os.getenv('DJANGO_ADMIN_URL', 'admin/')

urlpatterns = [
    path('', include('users.urls')),
    path('', include('artworks.urls')),
    path('', include('collections_app.urls')),
    path(admin_route, admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
