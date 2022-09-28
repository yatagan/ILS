from django.shortcuts import render,redirect
from core.models import Author, Book, BookInstance
from warehouse.models import Rack
from warehouse.forms import AddBookInstanceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    #warehouse`s main page`
    context ={'unracked_books': BookInstance.objects.all(), 
              'racks': Rack.objects.filter(title__isnull=False)} 
    return render(request, 'warehouse/index.html', context)

def list_items(request):
    
    context ={'unracked_books': BookInstance.objects.all(), 
              'racks': Rack.objects.filter(title__isnull=False)} 
    return render(request, 'warehouse/list_items.html', context)

@login_required
def add_book_instance(request):
    librarians = User.objects.filter(is_staff=1)
    for librarian in librarians:
        if request.user == librarian:
            if request.method != 'POST':
                form = AddBookInstanceForm()
            else:
                form = AddBookInstanceForm(data=request.POST)

            if form.is_valid():
                selected_book = form.cleaned_data['book']
                format_book = form.cleaned_data['format_book']
                number = form.cleaned_data['number']
                rack = form.cleaned_data['rack']
                new_books = [BookInstance(book=selected_book, format_book=format_book) for _ in range(number)]
                for book in new_books:
                    book.save()
                    rack.books.add(book)
                rack.save()
                return redirect ('warehouse:index')
   
    context = {'form': form}
    return render(request, 'warehouse/add_book_instance.html', context)


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
                                 

    

    