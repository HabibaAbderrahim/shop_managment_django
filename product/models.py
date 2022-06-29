from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=200 , null = True)
    price = models.FloatField(null=True)
    date_create = models.DateTimeField(null=True, auto_now_add=True)
