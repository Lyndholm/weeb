from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),

    path('artwork/<uuid:pk>/', views.artwork_page, name='artwork'),
    path('artwork/create/', views.create_artwork, name='artwork-create'),
    path('artwork/<uuid:pk>/edit/', views.edit_artwork, name='artwork-edit'),
    path('artwork/<uuid:pk>/delete/', views.delete_artwork, name='artwork-delete'),
    path('artwork/<uuid:pk>/favorite/', views.favorite_artwork, name='artwork-favorite'),
    path('artwork/<uuid:pk>/unfavorite/', views.unfavorite_artwork, name='artwork-unfavorite'),

    path('tags/', views.tags_page, name='tags'),

    path('search/', views.search_page, name='search'),

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
