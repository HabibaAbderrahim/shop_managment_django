
from dataclasses import fields
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model= Product
        fields = '__all__'
        exclude = ['name','date_create','tag','image_product']

    


