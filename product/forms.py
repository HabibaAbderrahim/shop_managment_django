
from logging import exception
from django.forms import ModelForm
from .models import Product 

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields= '__all__'
        exclude = ['image_product']
       