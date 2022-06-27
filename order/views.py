from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def list_order(request):
    return HttpResponse("Order page")