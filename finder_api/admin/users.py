from django.contrib import admin

# Register your models here.
from typing import ClassVar

from finder_api.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class FavoritesInline(admin.TabularInline):
    model = User.favorites.through
    extra = 1

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Base JSON."""

    list_display: ClassVar = [
        "username",
        "email",
        "is_staff",
    ]
    
    BaseUserAdmin.fieldsets[0][1]["fields"] += ("uuid","is_public")
    fieldsets: ClassVar = [
        *list(BaseUserAdmin.fieldsets),
    ]
    inlines=[FavoritesInline]
    readonly_fields=["uuid"]