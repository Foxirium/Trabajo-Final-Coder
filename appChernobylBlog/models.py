from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.


#---------------------------------------ModeloPost---------------------------------------#
class Category (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name




class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(auto_now_add = True)
    category =models.CharField(max_length=255, default= 'category')


    def __str__(self):
        return self.title + ' | '+ str(self.author)


        