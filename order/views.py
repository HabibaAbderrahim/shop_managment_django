from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import OrderForm
from product.views import manage
from .models import Order

# Create your views here.

def list_order(request):
    return render(request ,'order\list_order.html')


def add_order(request):
    #call empty form
    form = OrderForm()
    if request.method=='POST':
        #render with data
        form = OrderForm(request.POST)
        if form.is_valid():
            #save data
            form.save()
            return redirect(manage)
    context={'forms':form}        
    return render(request ,'order\order_add.html',context)


def modify_order(request , pk):
    order= Order.objects.get(id=pk)
    #call form with specif product
    form = OrderForm(instance=order)
    if request.method=='POST':
        #save posted data and product instance
        form = OrderForm(request.POST , instance=order) 
        if form.is_valid():
            form.save()
            return redirect(manage)
    context={'forms':form}      
    #where the form is  
    return render(request ,'order\order_add.html',context)


def delete_order(request ,pk):
    order=Order.objects.get(id=pk)
    #based on request
    if request.method=='POST':
        order.delete()
        return redirect(manage)
    context={'order':order}
    return render(request ,'admin\manage.html' )
