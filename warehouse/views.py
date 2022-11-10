from django.shortcuts import render,redirect
from core.models import Author, Book, BookInstance
from warehouse.models import Rack
from warehouse.forms import AddBookInstanceForm, ReturnInstanceForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from visitors.models import Librarian
from django.core.paginator import Paginator



@login_required
def index(request):
    NUMBER_ITEMS_ON_PAGE = 10
    if Librarian.objects.filter(id=request.user.id).exists():
        page_num = (request.GET.get('page', 1))
        book_items = BookInstance.objects.all().order_by('pk')
        paginator = Paginator(book_items, NUMBER_ITEMS_ON_PAGE)
        page_obj = paginator.get_page(page_num)
        context ={'page_obj': page_obj} 
        return render(request, 'warehouse/index.html', context)
    else:
        return HttpResponse("У Вас не має таких прав", status=401) 



@login_required
def list_items(request):
    NUMBER_ITEMS_ON_RACK = 1
    if Librarian.objects.filter(id=request.user.id).exists():
        page_num = (request.GET.get('page', 1))
        racks = Rack.objects.filter(title__isnull=False).order_by('pk')
        paginator = Paginator(racks, NUMBER_ITEMS_ON_RACK)
        page_obj = paginator.get_page(page_num)
        context ={'page_obj': page_obj} 
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
                status = form.cleaned_data['status']
                number = form.cleaned_data['number']
                isbn = form.cleaned_data['isbn']
                rack = form.cleaned_data['rack']
                new_books = [
                    BookInstance(
                        book=selected_book,
                        format_book=format_book,
                        status=status,
                        isbn=isbn,
                        rack=rack,
                    ) for _ in range(number)
                ]
                for book in new_books:
                    book.save()
                    rack.books.add(book)
                messages.success(request, "Екземпляр книги успішно додано")
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
                return_instance = BookInstance.objects.get(id=instance_id)
                
                if return_instance.status == 'o':
                    return_instance.status = 'a'
                    return_instance.save()
                    messages.success(request, "Книгу повернуто в бібліотеку")    
                    return redirect ('warehouse:return_instance')
                
                else:
                    messages.error(request, "Не можливо повернути цю книгу, бо вона не була видана.")
                    return redirect ('warehouse:return_instance')
         
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
                                 

    

    
