from django.urls import path

from .views import (
    CustomLoginView,
    CustomLogoutView,
    MyProfile,
    ProfilePage,
    RegistrationView,
    placeholder_view,
)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),

    path('me/', MyProfile.as_view(), name='my-profile'),
    path('profile/<uuid:pk>/', ProfilePage.as_view(), name='user-profile'),

    path('', placeholder_view, name='placeholder'),
]
