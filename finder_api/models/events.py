from uuid import uuid4
from django.db import models


class Event(models.Model):

    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(verbose_name="Name of the event",max_length=255)
    description = models.CharField(verbose_name="Description of the event",max_length=255)

    location = models.CharField(verbose_name="Location of the Event",max_length=255)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    is_public = models.BooleanField(default=False)
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Events"

    def get_logo(self):
        try:
            return self.logo.url.removeprefix("/finder_api")
        except ValueError:
            return ""
    
    def __str__(self):
        return self.name