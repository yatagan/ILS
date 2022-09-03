from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    def get_books(title):
        return Book.objects.filter(title__contains=title)
# get_books('Java')
# [list of Java books]
# get_books('Python')
# [list of Python book]

class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    number = models.IntegerField(default=0)

    def check_book_title(title):
        """
            >>> check_book_title("wsadfsadf")
            Вибачте, такої книги не має в нашій бібліотеці.
            >>> check_book_title("Head")
            {'Headfirst Java': 2, 'Head fist Python': 13}
        """
        books = Book.objects.filter(title_contains=title)
        book_dicsh = {}
        book_dicsh = dict(books)
        print(book_dicsh)
         
        if books:
            return f"Вибачте, такої книги не має в нашій бібліотеці."
        else:
            return BookInstance.objects.filter()
        

    def number_books(self):
        return self.bookinstance_set.count()
        #if instance == 0:
        #   return f"All of theese books are in rent!"
        #else:
        #   return f"Book rental available" 

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} (#{self.id})"


# class BookRent(models.Model):
#     books = models.ManyToManyField(BookInstance)
#     visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
#     active = models.BooleanField()
#     date = models.DateField()
#     date_off = models.DateField()

class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.title

class Library(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title    


class Catalog(models.Model):

    def __str__(self):
        return self

class  Rack(models.Model):

    def __str__(self):
        return self    



                                

