
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db import models

from finder_api.models.restaurant import Restaurant




class User(AbstractUser):
    
    
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    favorites = models.ManyToManyField("Restaurant", related_name='restaurants', blank=True)
    is_public = models.BooleanField(default=False)

    class Meta:
        db_table = "auth_user"
        ordering = ["username"]

    def dict(self):
        return {
            "name":self.username,
            "date":self.date_joined,
        }

    def add_to_favorites(self, uuid):
        self.favorites.add(Restaurant.objects.get(uuid))
        self.save()