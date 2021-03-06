import imp
from itertools import product
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render

from order.models import Order
from .models import Client
from order.models import Order
from product.models import Product
from .forms import ClientForm
from product.views import manage
from .filters import ClientFilter
# Create your views here.

#this render a commun template for all without id client
# def list_client(request):
#     return render(request ,'client\list_client.html')

#pk to get client id with him details
def list_client(request ,pk):
    #get client with that specific key
    clientKey=Client.objects.get(id=pk) 
    #orders of specific client:client product
    ordersList=clientKey.order_set.all()
    #filter
    filterClient= ClientFilter(request.GET , queryset=ordersList)
    #update List
    ordersList = filterClient.qs
    #total
    total = ordersList.count()
    context ={'clientX':clientKey ,'ordersList':ordersList,'total':total , 'filterClient':filterClient}
    return render(request ,'client\list_client.html',context)

def add_client(request):
    #call empty form
    form = ClientForm()
    if request.method=='POST':
        #render with data
        form = ClientForm(request.POST)
        if form.is_valid():
            #save data
            form.save()
            return redirect(manage)
    context={'formClient':form}        
    return render(request ,'client\client_add.html',context)



