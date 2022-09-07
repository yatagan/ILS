from django.shortcuts import render
from .models import Book, BookInstance, Post
from django.db.models import Q



def index(request):
    """Home page library."""
    posts = Post.objects.all()
    return render(request, 'core/index.html', {'posts': posts})

def search_books(request):
    search_query = request.GET.get('search', '')
    if search_query:
        books = Book.objects.filter(Q(title__icontains=search_query) | Q(authors__name__icontains=search_query)).distinct()
    else:
    #show all books
        books = Book.objects.all()
            
    context = {'books': books.order_by('title')}
    return render(request, 'core/search_results.html', context)

# def new_order(request):
#     book = BookInstance.objects.get()
#     if book:
#         form = OrderForm(request.POST)
#         # if form.is_valid():
#         #     new_order = form.save()
#         #     new_order.book = book
#         #     new_order = save()
        
  
#     context = {'order': order, 'form': form}
#     return render(request, 'core/new_order.html', context)