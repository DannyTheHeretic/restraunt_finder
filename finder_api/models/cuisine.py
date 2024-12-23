
from django.db import models


class Cuisine(models.Model):
    
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name