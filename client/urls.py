from django.urls import path
from . import views

urlpatterns = [
    #the name is used for links 
    #/client/pk=id
    path('<str:pk>',views.list_client,name='clientDetails'),
]
