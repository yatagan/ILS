from django.db import models
from core.models import BookInstance

# Create your models here.
class  Rack(models.Model):
    books = models.ManyToManyField(BookInstance)
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.number_rack    