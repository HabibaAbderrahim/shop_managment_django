from django.http import HttpResponse
from django.shortcuts import render
from .forms import OrderForm

# Create your views here.

def list_order(request):
    return render(request ,'order\list_order.html')


def add_order(request):
    #call form
    form = OrderForm()
    return render(request ,'order\order_add.html')