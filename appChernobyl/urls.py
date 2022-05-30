from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
from appChernobylBlog.views import *

urlpatterns = [
    
    path('', inicio, name = 'inicio'),
    path('stalkers2/', stalkers2, name = 'stalkers2'),
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
    #path('post/', post, name = 'Post'),
    path('', HomeView.as_view(), name="post_home"),
    path('crearPost/', crearPost, name= 'crearPost'),


#URL CRUD STALKER

    path('stalker/nuevo/', StalkerCreate.as_view(), name='stalker_crear'),
    path('stalker/<pk>', StalkerDetail.as_view(), name='stalker_detalle'),
    path('stalker/list/', StalkerList.as_view(), name='stalker_listar'),
    path('stalker/editar/<pk>', StalkerUpdate.as_view(), name='stalker_editar'),
    path('stalker/borrar/<pk>', StalkerDelete.as_view(), name='stalker_borrar'),

#URL CRUD POST

    path('post/nuevo/', PostCreate.as_view(), name='post_crear'),
    path('post/<pk>', PostDetail.as_view(), name='post_detalle'),
    path('post/list/', PostList.as_view(), name='post_listar'),
    path('post/editar/<pk>', PostUpdate.as_view(), name='post_editar'),
    path('post/borrar/<pk>', PostDelete.as_view(), name='post_borrar'),

    path('padre/', padre, name='padre'),



    path('stalkers/', stalkers, name = 'stalkers'),
]