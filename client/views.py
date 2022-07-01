from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from order.models import Order
from .models import Client
from order.models import Order
# Create your views here.

#this render a commun template for all without id client
# def list_client(request):
#     return render(request ,'client\list_client.html')

#pk to get client id with him details
def list_client(request ,pk):
    #get client with that specific key
    clientKey=Client.objects.get(id=pk)
    #orders of specific client
    ordersList=clientKey.order_set.all()
    context ={'clientX':clientKey ,'ordersList':ordersList}
    return render(request ,'client\list_client.html',context)