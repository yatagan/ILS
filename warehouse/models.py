from django.db import models
from core.models import BookInstance

# Create your models here.
class  Rack(models.Model):
    number_rack = models.IntegerField(default=0)
    number_shell = models.IntegerField(default=0)

    def __str__(self):
        return self.number_rack    