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
    #total
    total = ordersList.count()
    context ={'clientX':clientKey ,'ordersList':ordersList,'total':total}
    return render(request ,'client\list_client.html',context)

def create_client(request):
    form = ClientForm()
    if request.method=="POST":
        form = ClientForm(request.POST)
        form.save()
        return redirect(manage)
    context={'form':form}
    return render(request ,'client\add_client.html',context)



