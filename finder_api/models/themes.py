
from django.db import models
from uuid import uuid4
from django.contrib import admin

class Themes(models.Model):
    
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, default="")
    region = models.CharField(max_length=255, default="")
    logo = models.URLField(max_length=511, default="", blank=True)

    class Meta:
        ordering = ["name"]

    @admin.display(
        boolean=True,
        ordering="Has Logo?",
        description="Does the catagory have a logo?",
    )
    def has_logo(self):
        return bool(self.logo)

    def __str__(self):
        return self.name