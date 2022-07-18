from http import client
import imp
from msilib import Table
from multiprocessing import context
from re import M
import string
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from client.models import Client
from order.models import Order
from product.models import Product
from tag.models import Tag
from .filters import ProductFilter
from django.db.models.functions import Lower
from django.db.models import Q
# Create your views here.
from order.models import Order
from .forms import ProductForm


def home(request ):
    pk=1
    products=Product.objects.all()
    #since we are getting products
    #Entry.objects.order_by(Lower('headline').desc())
    filters= ProductFilter(request.GET, queryset=products)
    #!!Update commands
    products=filters.qs
   
    
    #dict key value
    context={'product':products,'filters':filters}

    #render template with data
    return render(request ,'product\home.html', context)



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
    #count
    #orders of specific product
    ordersList=productX.order_set.all()
    #total
    total = ordersList.count()

    context ={'productx':productX , 'tagx':tagX , 'tot':total}

    return render(request,'product\single.html',context)   


def addProduct(request):
    #call empty form
    form = ProductForm()
    if request.method=='POST':
        #render with data
        form = ProductForm(request.POST)
        if form.is_valid():
            #save data
            form.save()
            return redirect(manage)
    context={'formP':form}        
    return render(request ,'product\product_add.html',context)



