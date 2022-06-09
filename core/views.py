from django.shortcuts import render, redirect
from .models import Book 
from .forms import BookForm


def index(request):
    """Home page app ILS."""
    return render(request, 'ILS/index.html')
    
def new_book(request):
    #додати нову книгу
    if request.method != 'POST':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('ils:book') #куди перенаправляти?:-)
    
    context = {'form': form}
    return render(request, 'core/new_book.html', context)

