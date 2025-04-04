from django.db import models
from uuid import uuid4


rate = [(i, i/10) for i in range(100)]

class Reviews(models.Model):
    
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.DO_NOTHING)
    user = models.ForeignKey("User", null=True, on_delete=models.SET_NULL)
    rating = models.IntegerField(choices=rate)
    review_text = models.TextField(default="")
    created_at = models.DateTimeField(verbose_name="Date Created", auto_now=True, blank=True)
    
    class Meta:
        ordering = ["rating"]
        verbose_name_plural = "Reviews"
        
        
    def dict(self):
        return {
            "id":self.uuid,
            "restaurant":self.restaurant.get().dict(),
            "user":self.user.get().dict(),
            "rating":self.rating,
            "review":self.review_text,
            "date":self.created_at,
        }
    
    def rating_score(self):
        return (self.rating/10)
    
    def __str__(self):
        return self.review_text