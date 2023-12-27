from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Post, Category, Comments, Likes

class GetPosts(ListView):
    model = Post
    template_name = ('app/index.html')
    context_object_name = 'posts'

class GetDetail(DetailView):
    model = Post

class CreatePost(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/prof'

class UpdatePost(UpdateView):
    model = Post

class DeletePost(DeleteView):
    model = Post
    success_url = '/prof'

def index(request):
    posts = Post.objects.all()
    likes = Likes.objects.all()
    com = Comments.objects.all()
    cats = Category.objects.all()
    return render(request, 'app/test.html', context={'posts': posts, 'likes': likes, 'comm': com, 'cats': cats})