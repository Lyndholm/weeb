from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('placeholder')

    def form_invalid(self, form):
        messages.error(self.request, 'Неверное имя пользователя или пароль.')
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class RegistrationView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('placeholder')

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
            return redirect('placeholder')

        return super().get(*args, **kwargs)


def placeholder_view(request):
    return render(request, 'main.html')
