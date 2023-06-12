from django.views.generic import ListView, DetailView
from .models import Post



class PostList(ListView):
    model = Post
    template_name = 'news/default.html'
    context_object_name = 'news'



class PostDetail(DetailView):
    model = Post
    template_name = 'news/index.html'
    context_object_name = 'new'
