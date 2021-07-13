from os import name
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100,default="no_name")
    material = models.CharField(max_length=30,blank=True)
    company = models.CharField(max_length=30,blank=True)
    type = models.CharField(max_length=30,blank=True)
    subcompany = models.CharField(max_length=30,blank=True)
    company = models.CharField(max_length=30,blank=True)
    size = models.CharField(max_length=30,blank=True)
    extra1 = models.CharField(max_length=30,blank=True)
    extra2 = models.CharField(max_length=30,blank=True)
    
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=9, decimal_places=2,blank=True,null=True)
    
    img1 = models.ImageField(upload_to="media",default="")
    img2 = models.ImageField(upload_to="media",blank=True,null=True)
    img3 = models.ImageField(upload_to="media",blank=True,null=True)
