"""
grocery_project URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('items.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
