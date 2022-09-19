from rest_framework import serializers
from items.models import Items
from django.contrib.auth.models import User

class ItemsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Items
        fields = ['id', 'groc_items', 'notes', 'item_price', 'item_pprice', 'budget', 'date_created', 'owner',]


    def create(self, validated_data):
        """
        Create and return a new `Items` instance, given the validated data.
        """
        return Items.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Items` instance, given the validated data.
        """
        #instance.title = validated_data.get('title', instance.title)
        instance.groc_items = validated_data.get('groc_items', instance.groc_items)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.item_price = validated_data.get('item_price', instance.item_price)
        instance.item_pprice = validated_data.get('item_pprice', instance.item_pprice)
        instance.budget = validated_data.budget('budget', instance.budget)
        instance.date_created = validated_data.date_created('date_created', instance.date_created)
        instance.save()
        return instance
class UserSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Items.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'items']