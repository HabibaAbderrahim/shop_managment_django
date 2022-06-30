from http import client
import imp
from itertools import product
from pyexpat import model
from django.db import models
from client.models import Client
from product.models import Product
# Create your models here.

class Order (models.Model):
    status_list=(("in production","in production"),("Shipped","Shipped"),("Delivered","Delivered"))
    #one to many
    client = models.ForeignKey(Client , null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product ,null=True , on_delete=models.SET_NULL)
    #choices 
    status = models.CharField(null=True, max_length=200,choices=status_list)
    date_create= models.DateTimeField(null=True, auto_now_add=True)
