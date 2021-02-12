from rest_framework import serializers

from .models import USER, INVENTORY, MOVIE, STORE, RENTAL

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = USER
        fields = ('User_id', 'Name', 'Surname', 'Email', 'Phone')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MOVIE
        fields = ('Movie_id', 'Name', 'Price')

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = STORE
        fields = ('Store_id', 'Address', 'Phone')

class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = INVENTORY
        fields = ('Item_id', 'ID_movie', 'ID_store', 'Quantity')

class RentalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RENTAL
        fields = ('ID_register', 'ID_store', 'ID_user', 'ID_item', 'Checkout_date', 'Return_date')
