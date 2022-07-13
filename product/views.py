from http import client
from msilib import Table
from multiprocessing import context
import string
from django.http import HttpResponse
from django.shortcuts import render
from client.models import Client
from order.models import Order
from product.models import Product
from tag.models import Tag
# Create your views here.

def home(request ):
    pk=1
    #findall from model
    clients= Client.objects.all()
    orders=Order.objects.all()
    products=Product.objects.all()
    #filtring
    tags=Product.objects.get(id=pk).tag.all()
    #dict key value
    context={'clients':clients,'orders':orders,'product':products,'tags':tags}

    #render template with data
    return render(request ,'product\home.html', context)

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