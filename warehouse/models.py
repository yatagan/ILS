from django.db import models
from core.models import BookInstance


class Rack(models.Model):
    books = models.ManyToManyField(BookInstance, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Поличка книг'
        verbose_name_plural = 'Полички книг'    
        ordering = ['title']        

