from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.name
    