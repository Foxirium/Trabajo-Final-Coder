from pdb import post_mortem
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


# Create your views here.

#Creamos clase HomeView y le pasamos ListView para que nos liste en el home todos los post
class HomeView(ListView):

    model = Post
    template_name = 'appChernobylBlog/home.html'

#Creamos clase PostDetail y le pasamos DetailView para que muestre en detalle ese post
class PostDetail(DetailView):

    model = Post
    template_name = 'appChernobylBlog/post_detail.html'   


class PostCreate(CreateView):

    model = Post
    form_class= PostForm
    success_url = reverse_lazy ('home')  


#