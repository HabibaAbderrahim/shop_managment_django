from http import client
from msilib import Table
from multiprocessing import context
import string
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from client.models import Client
from order.models import Order
from product.models import Product
from tag.models import Tag
from .filters import ProductFilter
from django.db.models.functions import Lower
# Create your views here.

def home(request ):
    pk=1
    products=Product.objects.all()
    tags=Product.objects.get(id=pk).tag.all()
    pp=Product.objects.order_by(Lower('price').desc())
    #Filter sorted By price
    #since we are getting products
    #Entry.objects.order_by(Lower('headline').desc())
    filters= ProductFilter(request.GET, queryset=products)
    #!!Update commands
    products=filters.qs
    #name contains 
    ProductName=Product.objects.filter(name__regex='^[A-Za-z]')
    
    #dict key value
    context={'product':products,'filters':filters,'tags':tags,'ProductName': ProductName}

    #render template with data
    return render(request ,'product\home.html', context)

def FilerByName(request):
    ProductName =Product.objects.filter(name__regex='^[A-Za-z]')
    context={'ProductName': ProductName}
    return context

def manage(request):
    clients= Client.objects.all()
    orders=Order.objects.all()
    products=Product.objects.all()
    context={'clients':clients,'orders':orders,'product':products}
    #render template with data
    return render(request ,'admin\manage.html', context)
    

def detail(request , pk) :
    productX = Product.objects.get(id=pk)
    #filter
    tagX =Product.objects.get(id=pk).tag.all()
    context ={'productx':productX , 'tagx':tagX}

    return render(request,'product\single.html',context)   