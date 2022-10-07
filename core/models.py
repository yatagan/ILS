from tabnanny import verbose
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    def get_books(title):
        return Book.objects.filter(title__contains=title)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Автори'    
        ordering = ['name']        


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    number = models.IntegerField(default=0)        

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'    
        ordering = ['title']

class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
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

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', verbose_name='Статус:')
    format_book = models.IntegerField(choices=FORMATS, verbose_name='Формат:')

    def __str__(self):
        return f"{self.book.title} (format: {self.format_book})"

    class Meta:
        verbose_name = 'Екземпляр книги'
        verbose_name_plural = 'Екземпляри книг'    
        ordering = ['book']    


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Повідомлення'
        verbose_name_plural = 'Повідомлення'    
        ordering = ['title']        


class Library(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title    


class Catalog(models.Model):

    def __str__(self):
        return self
