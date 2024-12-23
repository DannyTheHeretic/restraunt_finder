

from uuid import uuid4
from django.db import models
from django.core.validators import RegexValidator



rate = [(i, i/10) for i in range(100)]


price = [
    (1, "Cheap (>5)"),
    (2, "Cheapish (5~10)"),
    (3, "Mid (10~15)"),
    (4, "Midish (15~30)"),
    (5, "Expensive (30~50)"),
    (6, "DAYUMM (50~100)"),
    (7, "Alright Then (100+)"),
]

class Restaurant(models.Model):

    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(verbose_name="Name of the Restaurant",max_length=255)
    lat = models.DecimalField(default=0,max_digits=9, decimal_places=6)
    long = models.DecimalField(default=0,max_digits=9, decimal_places=6)
    
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=63, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    website = models.URLField(blank=True)
    average_rating = models.IntegerField(choices=rate)
    price_level = models.IntegerField(choices=price,blank=True)
    catagory = models.ManyToManyField('Cuisine',blank=True)

    class Meta:
        ordering = ["name"]


    def dict(self):
        try:
            logo= f"https://logo.clearbit.com/{self.website.split("www.")[1].split("/")[0]}/"
        except IndexError:
            logo = ""
        return {
            "id": self.uuid,
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "phone": self.phone_number,
            "website": self.website,
            "rating": self.average_rating,
            "price_level": self.price_level,
            "catagory": [i.name for i in self.catagory.all()],
            "logo": logo
        }
    
    def __str__(self):
        return self.name