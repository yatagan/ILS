from django.shortcuts import render,redirect
from core.models import Book, BookInstance
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

    

    