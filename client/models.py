from django.db import models
from django.forms import CharField

# Create your models here.
class Client(models.Model):
    name= models.CharField(null=True, max_length=200)
    phone =models.CharField(null=True, max_length=50)
    date_create =models.DateTimeField(null=True, auto_now_add=True)
    
    def __str__(self):
        return self.name
    


#control how name is shown in consol
    