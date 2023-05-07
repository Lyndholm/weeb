from django.urls import path

from . import views

urlpatterns = [
    path('collections/', views.collections_home_page, name='collections'),
    path('collections/create/', views.create_collection, name='collection-create'),
]
