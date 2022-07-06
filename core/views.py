from django.shortcuts import render
from .models import Book, Post
from .forms import BookForm


def index(request):
    """Home page library."""
    posts = Post.objects.all()
    return render(request, 'core/index.html', {'posts': posts})

    