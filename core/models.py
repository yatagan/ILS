from email.policy import default
from unicodedata import name
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def number_books():
        instance = int(Book.number - Visitor.number)
        if instance == 0:
            return f"All of theese books are in rent!"
        else:
            return f"Book rental available" 

    

class Visitor(models.Model):
    name = models.CharField(max_length=200)
    #order = models.CharField(max_length=200)
    number = models.ImageField(default=1)
    #date_added = models.DateTimeField(auto_now_add=True)

    def chek_name():
        if name == name:
            pass

    def __str__(self):
        return self() 


class BookRent(models.Model):
    books = models.ManyToManyField(BookInstance)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    active = models.BooleanField()
    date = models.DateField()

