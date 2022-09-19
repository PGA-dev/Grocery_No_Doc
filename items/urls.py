from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from items import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('items/',
        views.ItemsList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>/',
        views.ItemsDetail.as_view(),
        name='items-detail'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])