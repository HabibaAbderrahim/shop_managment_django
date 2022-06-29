from http import client
from itertools import product
from django.db import models

# Create your models here.

class Order (models.Model):
    status_list=(("in production","in production"),("Shipped","Shipped"),("Delivered","Delivered"))
    # client =
    # product =
    #choices 
    status = models.CharField(null=True, max_length=200,choices=status_list)
    date_create= models.DateTimeField(null=True, auto_now_add=True)
