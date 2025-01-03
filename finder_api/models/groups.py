

from uuid import uuid4
from django.db import models

class Group(models.Model):

    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(verbose_name="Name of the group",max_length=255)
    
    users = models.ManyToManyField("User", related_name='users')
    events = models.ManyToManyField("Event",related_name='events')
    invites = models.ManyToManyField("Invite",related_name='invites')

    description = models.CharField(verbose_name="Description of the group",max_length=255)
    
    
    is_public = models.BooleanField(default=False)
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name