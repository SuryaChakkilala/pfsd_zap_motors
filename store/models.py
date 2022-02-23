from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(default='desc')

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url

class Order(models.Model):
    user = models.TextField(default='_')
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    product_name = models.TextField(default='_')

    def __str__(self):
        return str(self.id)