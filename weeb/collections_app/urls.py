from django.urls import path

from . import views

urlpatterns = [
    path('collections/', views.collections_home_page, name='collections'),
    path('collections/my', views.user_collections, name='my-collections'),
    path('collections/create/', views.create_collection, name='collection-create'),
    path('collections/<uuid:pk>/', views.collection_page, name='collection'),
    path('collections/<uuid:pk>/edit/', views.edit_collection, name='collection-edit'),
    path(
        'collections/<uuid:pk>/delete/',
        views.delete_collection,
        name='collection-delete',
    ),
    path(
        'collections/<uuid:pk>/add/',
        views.add_artwork_to_collection,
        name='collection-add-artwork',
    ),
    path(
        'collections/<uuid:pk>/remove/',
        views.remove_artwork_from_collection,
        name='collection-remove-artwork',
    ),
]
