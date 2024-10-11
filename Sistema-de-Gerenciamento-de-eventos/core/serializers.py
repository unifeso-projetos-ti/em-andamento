from core.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class EventAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAddress
        fields = ['cidade', 'estado', 'pais', 'cep']


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ['quantidade', 'valor']


class EventsSerializer(serializers.ModelSerializer):
    event_address = EventAddressSerializer(many=True, read_only=True)
    tickets = TicketsSerializer(many=True, read_only=True)
    class Meta:
        model = Events
        fields = '__all__'
