from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm

class IndexView(ListView):
  model = Post
  template_name = "index.html"
  ordering = ["-post_date"]

class PostView(DetailView):
  model = Post
  template_name = "post.html"

class CreatePostView(LoginRequiredMixin, CreateView):
  raise_exception = True
  model = Post
  form_class = PostForm
  template_name = "add_post.html"

class UpdatePostView(LoginRequiredMixin, UpdateView):
  raise_exception = True
  model =  Post
  form_class = PostForm
  template_name = "edit_post.html"

class DeletePostView(LoginRequiredMixin, DeleteView):
  raise_exception = True
  model = Post
  template_name = "delete_post.html"
  success_url = reverse_lazy("index")
