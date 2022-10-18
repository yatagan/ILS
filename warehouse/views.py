from django.shortcuts import render,redirect
from core.models import Author, Book, BookInstance
from warehouse.models import Rack
from warehouse.forms import AddBookInstanceForm, ReturnInstanceForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from visitors.models import Librarian


@login_required
def index(request):
    if Librarian.objects.filter(id=request.user.id).exists():
    #warehouse`s main page`
        context ={'unracked_books': BookInstance.objects.all(), 
                   'racks': Rack.objects.filter(title__isnull=False)} 
        return render(request, 'warehouse/index.html', context)
    else:
        return HttpResponse("У Вас не має таких прав", status=401) 


@login_required
def show_response_return(request):
    return render(request, 'warehouse/show_response_return.html')


@login_required
def list_items(request):
    if Librarian.objects.filter(id=request.user.id).exists():
        context ={'unracked_books': BookInstance.objects.all(), 
                 'racks': Rack.objects.filter(title__isnull=False)} 
        return render(request, 'warehouse/list_items.html', context)
    else:
        return HttpResponse("У Вас не має таких прав", status=401)


@login_required
def add_book_instance(request):
    if Librarian.objects.filter(id=request.user.id).exists():
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
    else:
         return HttpResponse("У Вас не має таких прав", status=401)


@login_required
def return_instance(request):
    if Librarian.objects.filter(id=request.user.id).exists():
        if request.method != 'POST':
            return_form = ReturnInstanceForm()
        else:     
            return_form = ReturnInstanceForm(data=request.POST)
            if return_form.is_valid():
                instance_id = return_form.cleaned_data['instance_id']
                return_book = BookInstance.objects.filter(id=instance_id)
                for return_instance in return_book:
                    return_instance.status = 'a'
                    return_instance.save()
                return redirect ('warehouse:show_response_return')
        ctx = {'return_form': return_form}
        return render(request, 'warehouse/return_instance.html', ctx)    
    else: 
        return HttpResponse("У Вас не має таких прав.", status=401)

@login_required
def search_book(request):
    search_query = request.GET.get('search', '')
    if search_query:
        books = Book.objects.filter(title__icontains=search_query).distinct()
    else:
        books = Book.objects.all()
    result_search_book = {'books': books}
    
    return render(request, 'warehouse/result_search.html', result_search_book)  


@login_required
def search_author(request):
    search_query = request.GET.get('search', '')
    if search_query:
        authors = Author.objects.filter(name__icontains=search_query).distinct()
    else:
        authors = Author.objects.all()
        
    result_search_author = {'authors': authors}     
    return render(request, 'warehouse/result_search.html', result_search_author)     
                                 

    

    