from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Post, Comments

# Create your views here.
class PostListView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'post_list'


class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post
    context_object_name = 'details'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
