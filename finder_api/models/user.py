
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):
    
    
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    favorites = models.ManyToManyField("Restaurant", related_name='restaurants')
    class Meta:
        db_table = "auth_user"
    
    def dict(self):
        return {
            "name":self.username,
            "date":self.date_joined,
        }
