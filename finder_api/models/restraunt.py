

from django.db import models
from django.core.validators import RegexValidator

price = [
    (1, "Cheap (>5)"),
    (2, "Cheapish (5~10)"),
    (3, "Mid (10~15)"),
    (4, "Midish (15~30)"),
    (5, "Expensive (30~50)"),
    (6, "DAYUMM (50~100)"),
    (7, "Alright Then (100+)"),
]

class Restraunt(models.Model):
    
    name = models.CharField(verbose_name="Name of the Restraunt",max_length=255)
    lat = models.DecimalField(default=0,max_digits=9, decimal_places=6)
    long = models.DecimalField(default=0,max_digits=9, decimal_places=6)
    
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=63)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list

    website = models.URLField()
    average_rating = models.DecimalField(decimal_places=2, max_digits=5)
    price_level = models.IntegerField(choices=price)
    catagory = models.ManyToManyField('Cuisine')

    def dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "phone": self.phone_number,
            "website": self.website,
            "rating": self.average_rating,
            "price_level": self.price_level,
            "catagory": [i.name for i in self.catagory.all()],
        }
    
    def __str__(self):
        return self.name