from django.db import models
from core.models import BookInstance
from visitors.models import Librarian, Member


class BookInstanceRent(models.Model):
    books = models.ManyToManyField(BookInstance)
    start_rent_date = models.DateField(auto_now=False)
    return_date = models.DateField(auto_now=False)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.books.get()}
           
    class Meta:
        verbose_name = 'Оренда книги'
        verbose_name_plural = 'Оренда книг'
        ordering = ['-id']


class BookInstanceOrder(models.Model):
    books = models.ManyToManyField(BookInstance)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    moment_reserve = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.books.get()}

    class Meta:
        verbose_name = 'Замовлення книги'
        verbose_name_plural = 'Замовлення книг'
        ordering = ['-id']
