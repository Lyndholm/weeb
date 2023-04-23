from django.contrib import admin
from .models import User, UserProfile


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


@admin.register(UserProfile)
class UserProfileModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
