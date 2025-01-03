from django.contrib import admin

# Register your models here.
from typing import ClassVar

from finder_api.models import Group

class UserInline(admin.TabularInline):
    model = Group.users.through
    extra = 1


class EventsInline(admin.TabularInline):
    model = Group.events.through
    extra = 1


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Base JSON."""
    
    search_fields = ["name", "description"]
    list_display = ["name",  "description"]

    fieldsets: ClassVar = [
        (
            None, {
                "fields": ("uuid",),
            },
        ),
        (
            "Features", {
                "fields":
                    (
                        "name",
                        "description",
                    )
                }
            ),
    ]
    inlines=[UserInline, EventsInline]
    readonly_fields = ["uuid"]
