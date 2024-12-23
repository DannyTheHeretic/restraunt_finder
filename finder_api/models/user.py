
from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):
    
    
    favorites = models.ManyToManyField("Restraunt", related_name='restraunts')
    class Meta:
        db_table = "auth_user"
        
