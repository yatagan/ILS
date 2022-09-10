from django.db import models
from core.models import BookInstance

# Create your models here.
class  Rack(models.Model):
    books = models.ManyToManyField(BookInstance)

    def __str__(self):
        return self.number_rack    