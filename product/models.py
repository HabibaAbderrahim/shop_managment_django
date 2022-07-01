import imp
from django.db import models
from tag.models import Tag
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=200 , null = True)
    price = models.FloatField(null=True)
    date_create = models.DateTimeField(null=True, auto_now_add=True)
    #many to many 
    tag=models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name
    
  