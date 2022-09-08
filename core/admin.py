from django.contrib import admin
from warehouse.models import *
from core.models import *

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)
# admin.site.register(BookRent)
admin.site.register(Post)
admin.site.register(Rack)
