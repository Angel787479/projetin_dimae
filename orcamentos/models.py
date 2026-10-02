from django.db import models

# Create your models here.
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    whatsapp = models.CharField(max_length=20)
    cep = models.CharField(max_length=10)
    senha = models.CharField(max_length=128)

class Orcamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lista_de_materiais = models.TextField()
    total_preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_frete = models.CharField(max_length=20)
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
