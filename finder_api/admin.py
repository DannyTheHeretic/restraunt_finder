from django.contrib import admin

# Register your models here.
from typing import ClassVar

from finder_api.models import User, Restaurant, Reviews, Cuisine
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class CuisineInline(admin.TabularInline):
    model = Restaurant.catagory.through
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


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """Base JSON."""


    fieldsets: ClassVar = [
        (
            "Features",
            {
                "fields": (
                    "uuid",
                    "name",
                    "address",
                    "city",
                    "country",
                    "phone_number",
                    "website",
                    "average_rating",
                    "price_level",
                    "logo",
                )
            },
        ),
    ]
    
    inlines=[CuisineInline]
    readonly_fields = ["uuid"]




@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    """Base JSON."""
    
    search_fields = ["name", "description"]
    list_display = ["name",  "description", "has_logo"]

    fieldsets: ClassVar = [
        ("Features", {"fields": ("name",
                                 "description", "logo")}),
    ]


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
