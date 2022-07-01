from http import client
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from client.models import Client
from order.models import Order
from product.models import Product
from tag.models import Tag
# Create your views here.

def home(request):
    #findall from model
    clients= Client.objects.all()
    orders=Order.objects.all()
    products=Product.objects.all()
    #dict key value
    context={'clients':clients,'orders':orders,'product':products}

    #render template with data
    return render(request ,'product\home.html', context)

def detail(request , pk) :
    productX = Product.objects.get(id=pk)
    #tag 
    tagX =Tag.objects.get(id=productX.id)
    context ={'productx':productX , 'tagx':tagX}

    return render(request,'product\single.html',context)   