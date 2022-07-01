from django.urls import path
from . import views

urlpatterns = [
    #the name is used for links 
    path('',views.list_client, name='clientDetails'),
]
