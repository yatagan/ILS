from django.db import models
from core.models import BookInstance


class Rack(models.Model):
    books = models.ManyToManyField(BookInstance)
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
