from typing import ClassVar

from finder_api.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html




@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Base JSON."""

    list_display: ClassVar = ["username", "email", "is_staff", "current_month_cost"]

    fieldsets: ClassVar = [
        *list(BaseUserAdmin.fieldsets),
    ]


