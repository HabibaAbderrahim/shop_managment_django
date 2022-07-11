from __future__ import all_feature_names
from dataclasses import field
import imp
from pyexpat import model
from django.forms import ModelForm
from .models import Order 

class OrderForm(ModelForm):
    class Meta:
        model = Order
        field = '__all__ '