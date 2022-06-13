from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    number = models.IntegerField(default=0)

    def number_books(self):
        return self.bookinstance_set.count()
                # if instance == 0:
        #     return f"All of theese books are in rent!"
        # else:
        #     return f"Book rental available" 

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    ISBN = models.CharField(max_length=13, default="I don't know what it is")
    number = models.IntegerField(default=0)
  

class Visitor(models.Model):
    name = models.CharField(max_length=200)
    order = models.CharField(max_length=200, default="this is my order")
    number = models.IntegerField(default=1)
    date_added = models.DateField(auto_now=True)

    # def chek_name(self):
    #     if self.name == self.name:
    #         pass


    def __str__(self):
        return self.name


class BookRent(models.Model):
    books = models.ManyToManyField(BookInstance)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    active = models.BooleanField()
    date = models.DateField()

