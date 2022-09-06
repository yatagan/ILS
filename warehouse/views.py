from django.shortcuts import render,redirect
from core.models import Author, Book, BookInstance
from .forms import BookForm
from django.http import HttpResponse


def index(request):
    #warehouse`s main page`
    return render(request, 'warehouse/index.html')

def new_book(request):
    if request.method != 'POST':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            # Input:   
            # Книжка (кобзар, пітон)
            # кількість екземплярів книжок (число)
            # створити кількість об'єктів BookInctance у кількості яка дорівнює кількості кількості екземплярів книжок (числу)
            # Кожен з цих екземплярів повинен містити об'єкт Книжка (кобзар, пітон) у своєму полі book
            selected_book = form.cleaned_data['book']
            кількість = form.cleaned_data['number']
            for _ in range(кількість):
                new_book = BookInstance(book=selected_book)
                new_book.save()

            return redirect ('warehouse:index')
    context = {'form': form}
    return render(request, 'warehouse/new_book.html', context)

def search_book(request):
    search_query = request.GET.get('search_book', '')
    if search_query:
        book = Book.objects.filter(title_incontains=search_query)
    else:
        book = Book.objects.all()
    result_search_book = {'search_query_book': book}
    # return HttpResponse(context)    
    return render(request, 'warehouse/result_search.html', result_search_book)  

def search_author(request):
    search_query = request.GET.get('search_author', '')
    if search_query:
        authors = Author.objects.filter(name_incontains=search_query)
    else:
        authors = Author.objects.all() 
    result_search_author = {'authors': authors}     
    return render(request, 'warehouse/result_search.html', result_search_author)     
                                 

    

    