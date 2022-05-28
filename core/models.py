from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    number = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Visitor(models.Model):
    name = models.CharField(max_length=200)


class BookRent(models.Model):
    books = models.ManyToManyField(BookInstance)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    active = models.BooleanField()
    date = models.DateField()
