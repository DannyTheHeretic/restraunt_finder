from django.contrib import admin

# Register your models here.
from typing import ClassVar

from finder_api.models import Restaurant


class CuisineInline(admin.TabularInline):
    model = Restaurant.catagory.through
    extra = 3


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

