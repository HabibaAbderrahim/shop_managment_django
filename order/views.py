from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def list_order(request):
    return render(request ,'order\list_order.html')


def add_order(request):
    return render(request ,'order\order_add.html')