from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('stalkers/', stalkers, name = 'stalkers'),
    path('factions/', factions_list, name = 'factions'),
    path('artifacts/', artifacts_list, name = 'artifacts'),
    path('levels/', levels, name = 'levels'),
    #path('formulario_stalkers/', formulario_stalkers, name= 'formulario_stalkers'),
    path('busqueda_stalkers/', busqueda_stalkers, name = 'busqueda_stalkers'),
    path('buscar/', buscar),
    path('login/', login_request, name='Login'),
    path('register/', register, name= 'Register'),
    path('logout/', LogoutView.as_view(template_name='appChernobyl/logout.html'), name= 'Logout'),
    path('editarPerfil/', editRegister, name='editarPerfil'),
    path('agregarAvatar/', AddAvatar, name='Agregar Avatar'),
    path('post/', post, name = 'Post'),
    path('crearPost/', crearPost, name= 'crearPost'),



    path('padre/', padre, name='padre'),
]