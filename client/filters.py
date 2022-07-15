from dataclasses import fields
from pyexpat import model
import django_filters
from order.models import Order

class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'
        exclude =['client',' date_create']