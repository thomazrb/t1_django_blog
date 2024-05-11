from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'homepage.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'