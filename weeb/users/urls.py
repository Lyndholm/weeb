from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegistrationView, placeholder_view

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),

    path('', placeholder_view, name='placeholder'),
]
