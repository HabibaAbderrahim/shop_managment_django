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
from django.db.models import Q
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

# def FilerByName(self, *args, **kwargs):     
#     qs = super(Product, self).FilerByName(*args, **kwargs) 
#     query = self.request.GET.get('q') 
#     if query: 
#         qs = self.model.objects.filter( 
#             Q(name__icontains=query) 
 
#         ) 
#         context={'filterName':qs}
#     return render(self ,'product\search.html', context)

       

# def FilerByName(request):
#     try:
#        query = int(request.GET.get('q'))
#     except:
#         query=None
#     qs= Product.objects.all()
#     if query  : 
#         qs = Product.objects.filter( 
#              Q(name__icontains=query) )
#     context={'filterName':qs}

#     return render(request ,'product\search.html', context)

def FilerByName(request):
    search_post = request.GET.get('search')
    if search_post:
        posts = Product.objects.filter(Q(name__icontains=search_post))
    else:
        # If not searched, return default posts
        posts = Product.objects.all().order_by("-date_create")
    context={'posts':posts}
    return render(request ,'product\search.html', context)
         
    

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