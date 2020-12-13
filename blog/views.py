from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Post

class BlogListView(ListView):
    model = Post
    template_name='home.html'

class BlogDetailView(ListView):
    model = Post
    template_name='post_detail.html'

class BlogCreateView(ListView):
    model = Post
    template_name='post_new.html'
    fields = ['title', 'author','body']

class BlogUpdateView(ListView):
    model = Post
    template_name='post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(ListView):
    model = Post
    template_name='post_delete.html'
    fields = reverse_lazy('home')

