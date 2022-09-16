from django.db import models
from core.models import BookInstance
from visitors.models import Librarian, Member

class BookInstanceRent(models.Model):
    books = models.ManyToManyField(BookInstance, verbose_name="Назва книги:")
    start_rent_date = models.DateField(auto_now=False)
    return_date = models.DateField(auto_now=False)
    librarian = models.ManyToManyField(Librarian, verbose_name="Книгу видав:")
    member = models.ManyToManyField(Member, verbose_name="Книгу отримав")
    




