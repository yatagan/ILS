from django.shortcuts import render,redirect
from core.models import Author, Book, BookInstance
from warehouse.forms import ManyBookInstanceForm
from warehouse.models import Rack





def index(request):
    #warehouse`s main page`
    context ={'unracked_books': BookInstance.objects.all(), 
              'racks': Rack.objects.filter(title__isnull=False)} 
    return render(request, 'warehouse/index.html', context)

def list_items(request):
    
    context ={'unracked_books': BookInstance.objects.all(), 
              'racks': Rack.objects.filter(title__isnull=False)} 
    return render(request, 'warehouse/list_items.html', context)


def new_item_book(request):
    if request.method != 'POST':
        form = ManyBookInstanceForm()
    else:
        form = ManyBookInstanceForm(data=request.POST)
        if form.is_valid():
            selected_book = form.cleaned_data['book']
            format_book = form.cleaned_data['format_book']
            number = form.cleaned_data['number']
            rack = form.cleaned_data['rack']
            new_book = [BookInstance(book=selected_book, format_book=format_book) for _ in range(number)] 
            for book in new_book:
                book.save()
                rack.books.add(book)
            return redirect ('warehouse:list_items', 'warehouse:index')

    context = {'form': form}
    return render(request, 'warehouse/new_item_book.html', context)

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
                                 

    

    