
from logging import raiseExceptions
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from appChernobyl.forms import Formulario_Stalkers, Formulario_Factions, Formulario_Artifacts, UserCreationForm, UserRegisterForm, UserEditForm, AddAvatar, Formulario_Posts
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

    #avatar = Avatar.objects.filter(user=request.user)#Me trae el objeto con el model avatar del usuario

    return render(request, 'appChernobyl/inicio.html') #{'avatar':avatar[0].avatar.url}) #traeme el primer elemento, que en este casi simepre es 1



def stalkers(request):

    return render(request, 'appChernobyl/stalkers.html')










#------------------------------------------------------------------------------------------------------
#Formulario stalkers

@login_required
def stalkers2(request):


    if request.method == 'POST': #Si entra por Post

            miFormulario = Formulario_Stalkers(request.POST)


            if miFormulario.is_valid(): #Si pasa la validacion
                informacion = miFormulario.cleaned_data
                stalker = Stalker (name=informacion['Name'], surname=informacion['Surname'], email=informacion['Email'], faction=informacion['Faction'], dateOfBirth=informacion['DateOfBirth']) #modelo=informacion[form]
                stalker.save()
                return render(request, 'appChernobyl/inicio.html') #Vuelvo a inicio

    else: #Si entra por Get


            miFormulario = Formulario_Stalkers() #Formulario Vacio

    return render(request, 'appChernobyl/stalkers2.html', {"miFormulario":miFormulario})    
#------------------------------------------------------------------------------------------------------




class StalkerList(LoginRequiredMixin, ListView):

    model = Stalker
    template_name = 'appChernobyl/stalker_list.html'

class StalkerDetail(LoginRequiredMixin, DetailView):

    model = Stalker
    template_name = 'appChernobyl/stalker_detalle.html'

class StalkerCreate(LoginRequiredMixin, CreateView):

    model = Stalker
    success_url = reverse_lazy ('stalker_listar')
    fields = ['name', 'surname','faction', 'email', 'dateOfBirth']    

class StalkerUpdate(LoginRequiredMixin, UpdateView):

    model = Stalker
    success_url = reverse_lazy ('stalker_listar')
    fields = ['name', 'surname','faction', 'email', 'dateOfBirth']


class StalkerDelete(LoginRequiredMixin, DeleteView): 

    model = Stalker
    success_url = reverse_lazy ('stalker_listar')
    fields = ['name', 'surname','faction', 'email', 'dateOfBirth']
    raise_exception = True       















#------------------------------------------------------------------------------------------------------
def busqueda_stalkers(request):

    return render(request, "appChernobyl/busqueda_stalkers.html")

#------------------------------------------------------------------------------------------------------
#Funcion para buscar un stalker
@login_required
def buscar(request):

    if request.GET["name"]:


        name = request.GET['name']
        stalkers = Stalker.objects.filter(name__icontains=name)

        return render(request, "appChernobyl/resultado_busquedastalkers.html", {"name":name, "stalkers":stalkers}) 

    else:

        return render(request, "appChernobyl/resultado_busquedastalkers.html") 


              




















#------------------------------------------------------------------------------------------------------

#Lista Facciones
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
##############################################LOGIN##############################################
@login_required
def levels(request):
    return render(request, 'appChernobyl/levels.html')        

#------------------------------------------------------------------------------------------------------
def login_request(request):

    if request.method =="POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            usuario=formulario.cleaned_data.get('username')
            contraseña=formulario.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)

                return render(request, "appChernobyl/inicio.html", {"mensaje":f"The zone greets you {usuario}"})

            else:
                return render(request, "appChernobyl/inicio.html", {"mensaje":"Datos Incorrectos"})

        else:

            return render(request, "appChernobyl/login.html", {"mensaje":"Error, Formulario Erroneo"})

    else:

        formulario=AuthenticationForm()
        return render(request, "appChernobyl/login.html", {'formulario':formulario})


#------------------------------------------------------------------------------------------------------
def register(request):
    if request.method =='POST':

        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():

            username=formulario.cleaned_data['username']
            formulario.save()

            return render(request, "appChernobyl/inicio.html", {"mensaje":"Succesful Register"})

    else:
        formulario = UserRegisterForm()

    return render(request, 'appChernobyl/register.html', {"formulario":formulario})


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

            return render(request, 'appChernobyl/inicio.html', {'user': user, 'mensaje': 'PERFIL MODIFICADO CON EXITO'})
        else:

            formulario = UserEditForm(initial={'email':user.email}) #ME DA YA EL MAIL QUE TENGO REGISTRADO


        return render(request, 'appChernobyl/editarPerfil.html', {'formulario':formulario, 'user':user})














#-----------------------------------------------------------------------------------------------------
##############################################AVATAR##############################################        



def agregarAvatar(request):

    user=User.objects.get(username=request.user)
    if request.method == 'POST':
        formulario=AddAvatar(request.POST, request.FILES) #Si viene por post lleno mi formulario con lo que trae el request, trae la imagen y el usuario, pero solo modifico la imagen
        if formulario.is_valid():
            #oldAvatar = Avatar.objects.filter()
            avatar=Avatar(user=user, avatar=formulario.cleaned_data['avatar'])
            avatar.save()
            return render(request, 'appChernobyl/inicio.html', {'user':user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE'})
    else:
        formulario=AddAvatar()
    return render(request, 'appChernobyl/agregarAvatar.html', {'formulario':formulario, 'user':user})




















#-----------------------------------------------------------------------------------------------------
##############################################POST##############################################    



def post(request):

    posts = Post.objects.filter(status = True)


    return render(request, "appChernobyl/post.html", {'posts':posts})



def crearPost(request):

    if request.method == 'POST': #Si entra por Post

            miFormulario = Formulario_Posts(request.POST, request.FILES)


            if miFormulario.is_valid(): #Si pasa la validacion
                informacion = miFormulario.cleaned_data
                crearPost = Post(title=informacion['title'], subtitle=informacion['subtitle'], body=informacion['body'], author=informacion['author'], date=informacion['date']) #modelo=informacion[form]
                crearPost.save()
                return render(request, 'appChernobyl/inicio.html', {"mensaje":"Post creado correctamente"}) #Vuelvo a inicio

    else: #Si entra por Get


            miFormulario = Formulario_Posts() #Formulario Vacio

    return render(request, 'appChernobyl/detallepost.html', {"miFormulario":miFormulario})    





def padre(request):
    return render(request, 'appChernobyl/padre.html')




#-----------------------------------------------------------------------------------------------------
##############################################CRUD POST##############################################    


class PostList(ListView):

    model = Post
    template_name = 'appChernobyl/post_list.html'

class PostDetail(DetailView):

    model = Post
    template_name = 'appChernobyl/post_detalle.html'

class PostCreate(CreateView):

    model = Post
    success_url = reverse_lazy ('post_listar')
    fields = ['title', 'subtitle','body', 'author', 'date']    

class PostUpdate(UpdateView):

    model = Post
    success_url = reverse_lazy ('post_listar')
    fields = ['title', 'subtitle','body', 'author', 'date']

class PostDelete(DeleteView): 

    model = Post
    success_url = reverse_lazy ('post_listar')
    fields = ['title', 'subtitle','body', 'author', 'date']      



#-----------------------------------------------------------------------------------------------------
         