from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import AddPostForm


class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.order_by('-posted_on')
    paginate_by = 6


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'
