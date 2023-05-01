from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('artwork/<uuid:pk>/', views.artwork_page, name='artwork'),
    path('artwork-create/', views.create_artwork, name='artwork-create'),
    path('artwork-edit/<uuid:pk>', views.edit_artwork, name='artwork-edit'),
    path('artwork-delete/<uuid:pk>/', views.delete_artwork, name='artwork-delete'),
    path('tags/', views.tags_page, name='tags'),
]
