from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView

from .forms import CustomUserCreationForm, ProfileUpdateForm
from .models import Profile, User


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home-page')

    def form_invalid(self, form):
        messages.error(self.request, 'Неверное имя пользователя или пароль.')
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class RegistrationView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(
                self.request, user, backend='django.contrib.auth.backends.ModelBackend'
            )

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'Введенные данные не прошли проверку. Пожалуйста, проверьте и исправьте ошибки.',
        )

        return super().form_invalid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home-page')

        return super().get(*args, **kwargs)


class MyProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'

    def get_object(self, queryset=None):
        return self.request.user


class ProfilePage(DetailView):
    model = User
    template_name = 'profile.html'


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('my-profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def dispatch(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile != request.user.profile:
            raise Http404  # TODO: Throw a 403 error or something else ???
        return super().dispatch(request, *args, **kwargs)
