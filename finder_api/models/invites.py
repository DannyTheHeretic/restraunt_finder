from django.db import models
from uuid import uuid4



class Invite(models.Model):
    
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    uses = models.IntegerField(default=0)
    created_by = models.ForeignKey("User", related_name="made_by",on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Date Created", auto_now=True, blank=True)
    
    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "Invites"

    def __str__(self):
        return self.uuid