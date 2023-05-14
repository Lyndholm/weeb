from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, User


@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_staff')

    def has_add_permission(self, request):
        return False


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
