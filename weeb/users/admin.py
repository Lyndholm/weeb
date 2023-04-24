from django.contrib import admin

from .models import Profile, User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
