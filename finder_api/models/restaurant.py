

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
    country = models.CharField(max_length=63, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    website = models.URLField(blank=True)
    average_rating = models.IntegerField(choices=rate, default=0)
    price_level = models.IntegerField(choices=price,blank=True)
    catagory = models.ManyToManyField('Cuisine',blank=True)
    logo = models.ImageField(upload_to="./finder_api/static/images/logos") 

    is_public = models.BooleanField(default=False)
    class Meta:
        ordering = ["name"]


    def dict(self):
        return {
            "id": self.uuid,
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "phone": self.phone_number,
            "website": self.website,
            "rating": self.average_rating,
            "price_level": price[self.price_level-1][1],
            "catagory": [i.name for i in self.catagory.all()],
            "logo": self.get_logo()
        }
    
    def get_logo(self):
        try:
            return self.logo.url.removeprefix("/finder_api")
        except ValueError:
            return ""
    
    
    def get_price(self):
        try:
            return price[self.price_level-1][1]
        except ValueError:
            return ""
    
    def loc_set(self):
        return self.lat > 1 or self.lat < -1
    
    def search(self):
        return f"{self.address}+{self.city}+{self.country}"

    def g_search(self):
        return f"{self.name}+{self.search()}"

    def __str__(self):
        return self.name