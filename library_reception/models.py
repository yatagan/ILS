from django.db import models
from core.models import BookInstance
from visitors.models import Librarian, Member

class BookInstanceRent(models.Model):
    books = models.ManyToManyField(BookInstance, verbose_name="Назва книги:")
    start_rent_date = models.DateField(auto_now=False)
    return_date = models.DateField(auto_now=False)
    librarian = models.ForeignKey(Librarian, verbose_name="Книгу видав:", on_delete=models.CASCADE)
    member = models.ForeignKey(Member, verbose_name="Книгу отримав", on_delete=models.CASCADE)

    def __str__(self):
        return  f"Книгу '{self.books}' отримав(ла) {self.member.first_name} {self.start_rent_date} числа."

    class Meta:
        verbose_name = 'Оренда книги'
        verbose_name_plural = 'Оренда книг'    
        ordering = ['member']    

class BookInstanceOrder(models.Model):
    #date_reserve = models.DateTimeField(verbose_name="Момент резервування")
    books = models.ManyToManyField(BookInstance, verbose_name="Назва книги:")
    member = models.ForeignKey(Member, verbose_name="Книгу замовив", on_delete=models.CASCADE)

    def __str__(self):
        return f"Книгу '{self.books}' замовив(ла) {self.member.first_name}."

    class Meta:
        verbose_name = 'Замовлення книги'
        verbose_name_plural = 'Замовлення книг'    
        ordering = ['member']    