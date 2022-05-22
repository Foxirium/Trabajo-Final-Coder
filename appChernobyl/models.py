from multiprocessing.dummy import current_process
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

#Creo clase stalker e importo modelos segun datos a introducir
class Stalker(models.Model):

    name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    faction = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    dateOfBirth = models.DateField(null=True)

    def __str__(self):
        return self.name+" "+self.surname+" - "+ self.faction     


#Creo clase factions e importo modelos segun datos a introducir
class Faction(models.Model):
    name = models.CharField(max_length=20, null=True)
    founder = models.CharField(max_length=30, null=True)
    leader = models.CharField(max_length=30, null=True)
    allies = models.CharField(max_length=100, null=True)
    neutral = models.CharField(max_length=100, null=True)
    enemies = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name+" - "+ self.founder   

#Creo clase artifacts e importo modelos segun datos a introducir
class Artifact(models.Model):

    name = models.CharField(max_length=30, null=True)
    price = models.CharField(max_length=30, null=True)
    advantage = models.CharField(max_length=100,null=True)
    disadvantage = models.CharField(max_length=100, null=True)
    dateOfBirth = models.DateField(null=True)

    def __str__(self):
        return self.name+" - "+ str(self.dateOfBirth)


#Creo clase levels e importo modelos segun datos a introducir
class Levels(models.Model):
    lName = models.CharField(max_length=30, null=True)
    lStructureAmount = models.IntegerField(null=True)
    lNpcAmount = models.IntegerField(null=True)
    difficulty = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.lName+" - "+ str(self.lNpcAmount)+" - "+ self.difficulty  


class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE) #usuario que hace referencia externa a otra clase, ese avatar va a pertenecer a un usuario (la ultima parte es "si borro el usuario, se borra el avatar")
    #SubCarpeta avatares de media

    avatar = models.ImageField(upload_to='avatar', null=True, blank = True)


#Clase models Posts
#Titulo que no pueda ser nulo ni dejado en blanco
#SubTitulo idem
#Body (instalado ckeditor, y de la libreria ckeditor.fields importardo RichTextField)
#autor(Ligado a una key, stalker. Si borra el usuario = stalker, se borran sus post tambien)
#imagen(Ingresar imagen)
#Date (Fecha creacion del post)

class Post(models.Model):

    title= models.CharField(null = False, blank= False, max_length= 50)
    subtitle= models.CharField(null= False, blank= False, max_length=100)
    body= RichTextField()
    author= models.CharField(null=False, blank = False, max_length=50, default='Random Stalker')
    date= models.DateField('Fecha de Creacion')
    status = models.BooleanField('Publish/Not Publish', default = True)


#Como los visualizo Titulo y Autor
    def __str__(self):
        return self.title + " - " + self.author


    
