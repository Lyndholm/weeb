from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'nickname',
            'biography',
            'avatar',
        )
