from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostListView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'post_list'


class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post
    context_object_name = 'details'

     
