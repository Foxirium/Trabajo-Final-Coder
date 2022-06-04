
from logging import raiseExceptions
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from appChernobyl.forms import Formulario_Stalkers, Formulario_Factions, Formulario_Artifacts, UserCreationForm, UserRegisterForm, UserEditForm, AddAvatar
from appChernobyl.models import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
#------------------------------------------------------------------------------------------------------

def inicio(request):


    return render(request, 'appChernobyl/inicio.html') 



def stalkers(request):

    return render(request, 'appChernobyl/stalkers.html')


#----------------------------------------------------------------------------------------------------------
##############################################CRUD STALKER##############################################


class StalkerList(LoginRequiredMixin, ListView):

    model = Stalker
    template_name = 'appChernobyl/stalker_list.html'

class StalkerDetail(LoginRequiredMixin, DetailView):

    model = Stalker
    template_name = 'appChernobyl/stalker_detalle.html'

class StalkerCreate(LoginRequiredMixin, CreateView):

    model = Stalker
    success_url = reverse_lazy ('stalker_listar')
    fields = ['name', 'surname','faction', 'dateOfBirth']    

class StalkerUpdate(LoginRequiredMixin, UpdateView):

    model = Stalker
    success_url = reverse_lazy ('stalker_listar')
    fields = ['name', 'surname','faction', 'dateOfBirth']


class StalkerDelete(LoginRequiredMixin, DeleteView): 

    model = Stalker
    success_url = reverse_lazy ('stalker_listar')
    fields = ['name', 'surname','faction', 'dateOfBirth']
    raise_exception = True       




#--------------------------------------------------------------------------------------------------------------------
##############################################Render Pag Buscar Stalker##############################################
def busqueda_stalkers(request):

    return render(request, "appChernobyl/busqueda_stalkers.html")


#----------------------------------------------------------------------------------------------------------
##############################################Buscar Stalker##############################################
@login_required
def buscar(request):

    if request.GET["name"]:


        name = request.GET['name']
        stalkers = Stalker.objects.filter(name__icontains=name)

        return render(request, "appChernobyl/resultado_busquedastalkers.html", {"name":name, "stalkers":stalkers}) 

    else:

        return render(request, "appChernobyl/resultado_busquedastalkers.html") 


            



#----------------------------------------------------------------------------------------------------------
##############################################Lista Facciones##############################################
def factions_list(request):

    factions = Faction.objects.filter()
    contexto = {"factions":factions}

    return render(request, "appChernobyl/factions.html", contexto)  




#-----------------------------------------------------------------------------------------------------
##############################################ARTEFACTOS##############################################



#Lista Artefactos 
def artifacts_list(request):

     artifacts = Artifact.objects.filter()
     contexto = {"artifacts":artifacts}

     return render(request, "appChernobyl/artifacts.html", contexto)


#-----------------------------------------------------------------------------------------------------
##############################################Levels Coming Soon##############################################




@login_required
def levels(request):
    return render(request, 'appChernobyl/levels.html')        

#-----------------------------------------------------------------------------------------------------
##############################################LOGIN##############################################
def login_request(request):

    if request.method =="POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            usuario=formulario.cleaned_data.get('username')
            contraseña=formulario.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)

                return render(request, "appChernobylBlog/blog_inicio.html", {"mensaje":f"The zone greets you {usuario}"})

            else:
                return render(request, "appChernobylBlog/blog_inicio.html", {"mensaje":"Datos Incorrectos"})

        else:

            return render(request, "appChernobyl/login.html", {"mensaje":"Wrong user or password, try again here"})

    else:

        formulario=AuthenticationForm()
        return render(request, "appChernobyl/login.html", {'formulario':formulario})


#-----------------------------------------------------------------------------------------------------------
##############################################Registro##############################################
def register(request):
    if request.method =='POST':

        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():

            username=formulario.cleaned_data['username']
            formulario.save()

            return render(request, "appChernobylBlog/blog_inicio.html", {"mensaje":"Succesfully Register"})

    else:
        formulario = UserRegisterForm()

    return render(request, 'appChernobyl/register.html', {"formulario":formulario})

#-----------------------------------------------------------------------------------------------------------
##############################################Editar Resgistro##############################################
@login_required
def editRegister(request):

        #Instancia Login
        user = request.user #traigo el usuario

        if request.method == 'POST': #si es por post
            formulario = UserEditForm(request.POST, instance=user) #traigo un formulario

            if formulario.is_valid(): #Si el formulario es valido

                information = formulario.cleaned_data # traigo la informacion del formulario

                #Datos ha modificar

                user.email = information['email']
                user.password1 = information['password1']
                user.password2 = information['password2']
                user.save() #guardo usuario con los datos guardados

            return render(request, 'appChernobylBlog/blog_inicio.html', {'user': user, 'mensaje': 'Stalker Profile Edit Success'})
        else:

            formulario = UserEditForm(initial={'email':user.email}) #ME DA YA EL MAIL QUE TENGO REGISTRADO


        return render(request, 'appChernobyl/stalker_profile_edit.html', {'formulario':formulario, 'user':user})


#------------------------------------------Coming Soon------------------------------------------------
##############################################AVATAR##############################################        
'''

def agregarAvatar(request):

    user=User.objects.get(username=request.user)
    if request.method == 'POST':
        formulario=AddAvatar(request.POST, request.FILES) #Si viene por post lleno mi formulario con lo que trae el request, trae la imagen y el usuario, pero solo modifico la imagen
        if formulario.is_valid():
            #oldAvatar = Avatar.objects.filter()
            avatar=Avatar(user=user, avatar=formulario.cleaned_data['avatar'])
            avatar.save()
            return render(request, 'appChernobylBlog/templateprueba.html', {'user':user, 'mensaje':'Avatar Created Succesfullu'})
    else:
        formulario=AddAvatar()
    return render(request, 'appChernobyl/agregarAvatar.html', {'formulario':formulario, 'user':user})

'''
