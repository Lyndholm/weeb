from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),

    path('artwork/<uuid:pk>/', views.artwork_page, name='artwork'),
    path('artwork/create/', views.create_artwork, name='artwork-create'),
    path('artwork/edit/<uuid:pk>/', views.edit_artwork, name='artwork-edit'),
    path('artwork/delete/<uuid:pk>/', views.delete_artwork, name='artwork-delete'),

    path('tags/', views.tags_page, name='tags'),

    path(
        'autocomplete/tags-with-create-new/',
        views.TagsAutocomplete.as_view(create_field='name'),
        name='autocomplete-tags-with-create-new',
    ),
    path(
        'autocomplete/tags-no-create-new/',
        views.TagsAutocomplete.as_view(),
        name='autocomplete-tags-no-create-new',
    ),
]
