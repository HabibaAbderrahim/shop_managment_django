from importlib.resources import path
from unicodedata import name

from django.urls import path 
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.list_order),
    path('add_order', views.add_order,name="add_order")
    path('modify_order/<str:pk>', views.modify_order , name="modify_order")
]
