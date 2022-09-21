from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from core.models import Author, Book, BookInstance
from .forms import ManyBookInstancesForm



def index(request):
    #warehouse`s main page`
    return render(request, 'warehouse/index.html')

@csrf_exempt
def new_book_naive(request):
    if request.method == 'GET':
        url = reverse('warehouse:new_book_naive')
        books = Book.objects.all()
        books_options = [f'<option value="{book.id}">{book.title}</option>' for book in books]
        formats_options = [f'<option value="{id}">{title}</option>' for id, title in BookInstance.FORMATS]

        form = f"""
            <form action="{url}" method=post>
                <select name="book">
                    {" ".join(books_options)}
                </select>
                <select name="format_book">
                    {" ".join(formats_options)}
                </select>
                <input name="isbn">
                <input type=submit>
            </form>
        """
        return HttpResponse(form)

    elif request.method == "POST":
        isbn = request.POST["isbn"]

        book_id = request.POST["book"]
        book = Book.objects.get(id=book_id)

        format_book = request.POST["format_book"]

        book = BookInstance.objects.create(book=book, isbn=isbn, format_book=format_book)

        return HttpResponse(book)

def new_book(request):
    if request.method != 'POST':
        form = ManyBookInstancesForm()
    else:
        form = ManyBookInstancesForm(data=request.POST)
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

            return redirect('warehouse:index')
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
                                 

    

    