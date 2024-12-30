from django.contrib import admin

# Register your models here.
from typing import ClassVar

from finder_api.models import Themes


@admin.register(Themes)
class ThemesAdmin(admin.ModelAdmin):
    """Base JSON."""
    
    search_fields = ["name", "description"]
    list_display = ["name",  "description", "has_logo"]

    fieldsets: ClassVar = [
        ("Features", {"fields": ("name",
                                "description", "logo")}),
    ]

