from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer, MovieSerializer, StoreSerializer, InventorySerializer, RentalSerializer
from .models import USER, MOVIE, INVENTORY, STORE, RENTAL

class UserViewSet(viewsets.ModelViewSet):
    queryset = USER.objects.all().order_by('User_id')
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MOVIE.objects.all().order_by('Name')
    serializer_class = MovieSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = STORE.objects.all().order_by('Address')
    serializer_class = StoreSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = INVENTORY.objects.all().order_by('Item_id')
    serializer_class = InventorySerializer

class RentalViewSet(viewsets.ModelViewSet):
    queryset = RENTAL.objects.all().order_by('ID_register')
    serializer_class = RentalSerializer

# Create your views here.
