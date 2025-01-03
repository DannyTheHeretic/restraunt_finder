
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db import models

from finder_api.models.restaurant import Restaurant


class UserFollowing(models.Model):
    user_id = models.ForeignKey("User", related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey("User", related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id','following_user_id'],  name="unique_followers")
        ]

        ordering = ["-created"]

    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"


class User(AbstractUser):
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    favorites = models.ManyToManyField("Restaurant", related_name='restaurants', blank=True)
    profile_image = models.ImageField(upload_to="./finder_api/static/images/profiles",blank=True)
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