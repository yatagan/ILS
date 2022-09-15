from django.shortcuts import render,redirect
from core.models import Author, Book, BookInstance
from .forms import BookForm



def index(request):
    #warehouse`s main page`
    return render(request, 'warehouse/index.html')

def new_book(request):
    if request.method != 'POST':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            selected_book = form.cleaned_data['book']
            кількість = form.cleaned_data['number']
            for _ in range(кількість):
                new_book = BookInstance(book=selected_book)
                new_book.save()

            return redirect ('warehouse:index')
    context = {'form': form}
    return render(request, 'warehouse/new_book.html', context)

def search_book(request):
    search_query = request.GET.get('search', '')
    if search_query:
        books = Book.objects.filter(title__icontains=search_query).distinct()
    else:
        books = Book.objects.all()
    result_search_book = {'books': books}
    
    return render(request, 'warehouse/result_search.html', result_search_book)  

def search_author(request):
    search_query = request.GET.get('search', '')
    if search_query:
        authors = Author.objects.filter(name__icontains=search_query).distinct()
    else:
        authors = Author.objects.all()
        
    result_search_author = {'authors': authors}     
    return render(request, 'warehouse/result_search.html', result_search_author)     
                                 

    

    