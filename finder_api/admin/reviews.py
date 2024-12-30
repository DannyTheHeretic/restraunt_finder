from django.contrib import admin

# Register your models here.
from typing import ClassVar

from finder_api.models import Reviews


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Base JSON."""

    list_display: ClassVar = [
        "restaurant", "user", "rating",
    ]

    fieldsets: ClassVar = [
        ("Features", {"fields": ("restaurant","user","rating","review_text","created_at")}),
    ]   
    readonly_fields = ["created_at"]
