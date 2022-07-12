from django.urls import path
from . import views

urlpatterns = [
    #the name is used for links 
    #/client/pk=id
    path('detail/<str:pk>',views.list_client,name='clientDetails'),
    path('add_client/new', views.add_client , name="add_client")
]
