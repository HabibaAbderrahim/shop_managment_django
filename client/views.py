from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Client
# Create your views here.

#this render a commun template for all without id client
# def list_client(request):
#     return render(request ,'client\list_client.html')

#pk to get client id with him details
def list_client(request ,pk):
    clientKey=Client.objects.get(id=pk)
    context ={'client':clientKey}
    return render(request ,'client\list_client.html',context)