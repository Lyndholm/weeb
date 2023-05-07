from django.urls import path

from . import views

urlpatterns = [
    path('collections/', views.collections_home_page, name='collections'),
    path('collections/my', views.user_collections, name='my-collections'),
    path('collections/create/', views.create_collection, name='collection-create'),
    path('collections/<uuid:pk>/edit/', views.edit_collection, name='collection-edit'),
    path('collections/<uuid:pk>/delete/', views.delete_collection, name='collection-delete'),
]
