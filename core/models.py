from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    def get_books(title):
        return Book.objects.filter(title__contains=title)


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    number = models.IntegerField(default=0)        

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=20, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Технічне обслуговування'),
        ('o', 'Видана'),
        ('a', 'Доступна'),
        ('r', 'Зарезервована'),
    )

    FORMATS = (
        (1, "paper"), 
        (2, "ebook"), 
        (3, "magazine"), 
        (4, "audio")
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m')
    format_book = models.IntegerField(choices=FORMATS)

    def __str__(self):
        return f"{self.book.title} (format: {self.format_book})"


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
