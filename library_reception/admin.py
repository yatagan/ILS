from django.contrib import admin

from .models import BookInstanceRent, BookInstanceOrder

admin.site.register(BookInstanceRent)
admin.site.register(BookInstanceOrder)
