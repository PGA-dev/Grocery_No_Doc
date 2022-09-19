# URLs for items
from django.urls import path
from items import views
from rest_framework.urlpatterns import format_suffix_patterns

""" 
API endpoints for Items and User List and Detail
These URLs are named to work with the HyperlinkedModelSerializer approach
with a single entry point functional view, the rest class based
"""


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('items/',
        views.ItemsList.as_view(),
        name='item-list'),
    path('items/<int:pk>/',
        views.ItemsDetail.as_view(),
        name='item-detail'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])