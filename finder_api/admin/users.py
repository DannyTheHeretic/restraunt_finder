from django.contrib import admin

# Register your models here.
from typing import ClassVar

from finder_api.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from finder_api.models.user import UserFollowing



class FavoritesInline(admin.TabularInline):
    model = User.favorites.through
    extra = 1

@admin.register(UserFollowing)
class UserFollowingAdmin(admin.ModelAdmin):

    list_display: ClassVar = [
        "user_id",
        "following_user_id",
    ]
    
    fieldsets: ClassVar = [
        ("Following", {"fields": ("user_id",
                    "following_user_id",)}),
    ]
    readonly_fields=["created"]
    

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