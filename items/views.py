from items.models import Items
from items.serializers import ItemSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from items.serializers import UserSerializer
from rest_framework import permissions
from items.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'items': reverse('items-list', request=request, format=format)
    })




class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer