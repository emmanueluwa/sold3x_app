from cgi import print_exception
import imp
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    thumbnail = models.URLField(max_length=500)
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=250)
    condition = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0)])
    sold_time = models.DateTimeField()
    listing_type = models.CharField(max_length=50)
