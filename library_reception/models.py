from django.db import models
from core.models import BookInstance

class BookInstanceRent(models.Model):
    books = models.ManyToManyField(BookInstance)
    start_rent_date = models.DateField(auto_now=False)
    return_date = models.DateField(auto_now=False)
    # status = models.ManyToManyField(BookInstance)

class LibraryCard(models.Model):

    def __str__(self):
        return self 

class Bookreservation(models.Model):

    def __str__(self):
        return self        
    
class Notification(models.Model):

    def __str__(self):
        return self      


