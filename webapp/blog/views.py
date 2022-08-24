from django.shortcuts import render
from .models import Post


# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def login(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/login.html', context)


def register(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/register.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})