
from django.db import models
from uuid import uuid4

class Cuisine(models.Model):
    
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    
    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name