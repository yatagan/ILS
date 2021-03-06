from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('warehouse/', include('warehouse.urls')),
    path('library_reception/', include('library_reception.urls')),
    path('visitors/', include('visitors.urls')),
]
