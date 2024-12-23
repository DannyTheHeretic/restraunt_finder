from django.contrib import admin

# Register your models here.
from typing import ClassVar

from finder_api.models import User, Restraunt, Reviews, Cuisine
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class CuisineInline(admin.TabularInline):
    model = Restraunt.catagory.through
    extra = 3

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Base JSON."""

    list_display: ClassVar = [
        "username",
        "email",
        "is_staff",
    ]

    fieldsets: ClassVar = [
        *list(BaseUserAdmin.fieldsets),
        ("Features", {"fields": ("favorites",)}),
    ]


@admin.register(Restraunt)
class RestrauntAdmin(admin.ModelAdmin):
    """Base JSON."""


    fieldsets: ClassVar = [
        (
            "Features",
            {
                "fields": (
                    "name",
                    "address",
                    "city",
                    "phone_number",
                    "website",
                    "average_rating",
                    "price_level",
                )
            },
        ),
    ]
    
    inlines=[CuisineInline]




@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    """Base JSON."""
    
    search_fields = ["name", "description"]
    list_display = ["name",  "description"]
    
    fieldsets: ClassVar = [
        ("Features", {"fields": ("name",
                                 "description")}),
    ]


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Base JSON."""

    list_display: ClassVar = [
        "restraunt", "user", "rating",
    ]

    fieldsets: ClassVar = [
        ("Features", {"fields": ("restraunt","user","rating","review_text","created_at")}),
    ]   
    readonly_fields = ["created_at"]
