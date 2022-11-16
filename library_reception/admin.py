from django.contrib import admin

from .models import BookLending, BookReservation

admin.site.register(BookLending)
admin.site.register(BookReservation)
