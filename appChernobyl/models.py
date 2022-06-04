from distutils.command.upload import upload
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














