from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import OrderForm
from product.views import manage

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