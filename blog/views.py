from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'homepage.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'author', 'content']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'content']