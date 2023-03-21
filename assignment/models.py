from django.db import models

# Create your models here.


class Product(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=200)
    price = models.FloatField()
    rating = models.FloatField()
    reviews = models.FloatField()
    description=models.TextField(max_length=400,blank=True,null=True)
    asin=models.CharField(max_length=100,blank=True,null=True)
    product_description=models.TextField(max_length=400,blank=True,null=True)
    manufacturer=models.CharField(max_length=100,blank=True,null=True)
