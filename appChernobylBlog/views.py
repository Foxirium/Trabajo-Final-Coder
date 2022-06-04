from pdb import post_mortem
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Mariano, Post, Comment, Profile
from .forms import PostForm, AddCommentForm

# Create your views here.


def home(request):
    
    return render(request, 'appChernobylBlog/blog_inicio.html', {})

#Creamos clase HomeView y le pasamos ListView para que nos liste en el home todos los post
class HomeView(ListView):

    model = Post
    template_name = 'appChernobylBlog/home.html'
#Ordeno por id del mas nuevo al mas viejo
    ordering = ['date']

#Creamos clase PostDetail y le pasamos DetailView para que muestre en detalle ese post
class PostDetail(DetailView):

    model = Post
    template_name = 'appChernobylBlog/post_detail.html'   

#Creamos clase PostCreate y le pasamos CreateView, form_class creado en form para darle estilo al formulario de creacion
class PostCreate(CreateView):

    model = Post
    form_class= PostForm
    success_url = reverse_lazy ('post_home') 

#Creamos clase PostUpdate y le pasamos Update, form_class creado en form para darle estilo al formulario de creacion
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



class CommentCreate(CreateView):

    model = Comment
    form_class = AddCommentForm
    template_name = 'appChernobylBlog/comment_form.html'
    success_url = reverse_lazy ('post_home') 


#Cuando un usuario crea un comentario, necesito ese formulario para relacionarlo con el post id. Si el formulario es correcto, necesito asociar la instancia del post id con la que se paso en la URL que se pasa como kwargs
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']

        return super().form_valid(form)





#Profile CRUD

class ProfileList(ListView):

    model = Profile
    template_name = 'appChernobylBlog/profile_list.html'

class ProfileDetail(DetailView):

    model = Profile
    template_name = 'appChernobylBlog/profile_detail.html'

class ProfileCreate(CreateView):

    model = Profile
    success_url = reverse_lazy ('post_home')
    fields = ['name', 'biography', 'image']

class ProfileUpdate(UpdateView):

    model = Profile
    success_url = reverse_lazy ('profile_list')
    fields = ['name', 'biography', 'image']


class ProfileDelete(DeleteView):

    model = Profile
    success_url = reverse_lazy ('profile_list')
    fields = ['name', 'bio', 'image']    

           


class AboutMeList(ListView):

    model = Mariano
    template_name = 'appChernobylBlog/aboutme_list.html'

