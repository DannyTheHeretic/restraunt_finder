

from datetime import datetime
from django.db import models
from uuid import uuid4


rate = [(i, i/10) for i in range(100)]

class Reviews(models.Model):
    
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.DO_NOTHING)
    user = models.ForeignKey("User", on_delete=models.DO_NOTHING)
    rating = models.IntegerField(choices=rate)
    review_text = models.TextField(default="")
    created_at = models.DateTimeField(verbose_name="Date Created", default=datetime.now, blank=True)
    
    def dict(self):
        return {
            "id":self.uuid,
            "restaurant":self.restaurant.get().dict(),
            "user":self.user.get().dict(),
            "rating":self.rating,
            "review":self.review_text,
            "date":self.created_at,
        }
    
    def __str__(self):
        return self.review_text