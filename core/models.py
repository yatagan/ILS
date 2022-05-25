from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    number = models.IntegerField(default=0)


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Visitor(models.Model):
    new_visitor = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)
    date = models.DateField()

