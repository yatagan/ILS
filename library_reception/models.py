from multiprocessing import context
from django.db import models
from django.shortcuts import render, redirect
from .forms import CardBookForm

def index(request):
    #library_reception home page
    return render(request, 'librery_reception/index.html')

def card_book_rent(request):
    #Change the form
    if request.method != 'POST':
        form = CardBookForm()
        context = {'form': form}
        return render(request, 'library_reception/card_book_rent.html', context)
    else:
        form = CardBookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('library_reception:card_book_rent.html')    
    


