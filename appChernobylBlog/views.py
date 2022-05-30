from pdb import post_mortem
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm


# Create your views here.


def home(request):
    
    return render(request, 'appChernobylBlog/templateprueba.html', {})

#Creamos clase HomeView y le pasamos ListView para que nos liste en el home todos los post
class HomeView(ListView):

    model = Post
    template_name = 'appChernobylBlog/home.html'
#Ordeno por id del mas nuevo al mas viejo
    ordering = ['-date']

#Creamos clase PostDetail y le pasamos DetailView para que muestre en detalle ese post
class PostDetail(DetailView):

    model = Post
    template_name = 'appChernobylBlog/post_detail.html'   

#Creamos clase PostCreate y le pasamos CreateView, form_class creado en form para darle estilo al formulario de creacion
class PostCreate(CreateView):

    model = Post
    form_class= PostForm
    success_url = reverse_lazy ('post_home') 

class PostUpdate(UpdateView):
    model = Post
    template_name = 'appChernobylBlog/post_update.html'
    success_url = reverse_lazy('post_home')
    form_class= PostForm   

class PostDelete(DeleteView):

    model = Post
    template_name= 'appChernobylBlog/post_delete.html'
    success_url = reverse_lazy('post_home')


#Funcion CategoryView, Busco que al tocar la categoria la misma me liste los post relacionados con esa categoria
#Filtro los atributos de mi post y busco las categorias
def CategoryView(request, cats):


    post_category = Post.objects.filter(category=cats)

    return render (request, 'appChernobylBlog/categories.html', {'cats': cats, 'post_category': post_category})







#