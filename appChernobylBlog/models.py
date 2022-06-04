from email.mime import image
from email.quoprimime import body_check
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

#---------------------------------------Categoria de Post---------------------------------------#
class Category (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#---------------------------------------Post---------------------------------------#   
class Post(models.Model):

    title = models.CharField(max_length=255)
    abstract = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    date = models.DateField(auto_now_add = True)
    category =models.CharField(max_length=255, default= 'category')

    def __str__(self):
        return self.title + ' | '+ str(self.author)


#---------------------------------------Profile---------------------------------------#
class Profile(models.Model):

   name = models.CharField(max_length=30)
   biography = RichTextField()
   image = models.ImageField(null=True, blank=True, upload_to="images/")
   date = models.DateField(auto_now_add = True)

   def __str__(self):
       return self.name + '  |  ' + str(self.date)

#---------------------------------------Comentarios---------------------------------------#
#Asocio el comentario con el post con el forignkey y agrego los campos que quiera que se vean
class Comment(models.Model):

    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE )
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title + ' | ' + self.name  

     



#---------------------------------------AboutMe---------------------------------------# 
 
class Mariano(models.Model):

    name = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    discord= models.URLField()
    youtube = models.URLField()
    body = RichTextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):

        return self.name 