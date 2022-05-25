from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
