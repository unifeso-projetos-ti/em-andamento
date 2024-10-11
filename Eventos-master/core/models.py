from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey('Tickets', on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cart'
        managed = False

class Events(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'events'
        managed = False

class EventAddress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    evento = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_address')
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=150)
    pais = models.CharField(max_length=150)
    cep = models.CharField(max_length=10)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'event_address'
        managed = False


class Tickets(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    evento = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='tickets')
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tickets'
        managed = False


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=150)
    pais = models.CharField(max_length=150)
    cep = models.CharField(max_length=10)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'address'
        managed = False


    