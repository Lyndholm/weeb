from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('artwork/<uuid:pk>/', views.artwork_page, name='artwork'),
    path('artwork-create/', views.create_artwork, name='artwork-create'),
]
