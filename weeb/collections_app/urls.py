from django.urls import path

from . import views

urlpatterns = [
    path('collections/create/', views.create_collection, name='collection-create'),
]
