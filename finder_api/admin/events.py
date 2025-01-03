from django.contrib import admin

# Register your models here.
from typing import ClassVar

from finder_api.models import Event


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    """Base JSON."""
    
    search_fields = ["name", "description"]
    list_display = ["name",  "description", "date"]

    fieldsets: ClassVar = [
        (
            None, {
                "fields": ("uuid","name","description",),
            },
        ),
        ("Details", {"fields": ("location","date", "time")}),
    ]
    
    readonly_fields=["uuid"]

