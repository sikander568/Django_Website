from django.db import models


# Create your models here.

class Contact(models.Model):
        # name = models.CharField(max_length=122)
        email =models.CharField(max_length=122)
        phone = models.CharField(max_length=15)
        desc = models.TextField()
        # date = models.DateTimeField(auto_now_add=True) 
        date = models.DateField()# Automatically sets the date when saved

def __str__(self):
    return self.name
    
    
