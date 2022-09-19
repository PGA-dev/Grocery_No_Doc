from rest_framework import serializer
from items.models import Items
from django.contrib.auth.models import User

class ItemsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')