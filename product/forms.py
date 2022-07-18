from dataclasses import fields
import imp
from pyexpat import model
from sqlite3 import PrepareProtocol
from django.forms import ModelForm
from .models import Product 

class ProductForm(ModelForm):
    class Meta:
        model = PrepareProtocol
        fields= '__all__'
       