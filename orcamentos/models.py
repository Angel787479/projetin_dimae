from django.db import models
from django.conf import settings 
from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    whatsapp = models.CharField(max_length=20)
    cep = models.CharField(max_length=10)
    senha = models.CharField(max_length=128)

    usuario = models.OneToOneField(settings.AUTH_USER_MODEL,
     on_delete=models.CASCADE, null=True, blank=True, 
     related_name='cliente')
    
    def __str__(self):
        return self.nome

class Orcamento(models.Model):
    FORMAS_RECEBIMENTO = [
            ("retirada", 'Retirada na loja'),
            ("entrega", 'Entrega na obra')
        ]
    STATUS_CHOICES = [
            ('salvo', 'Salvo'),
            ('aprovado', 'Aprovado'),
            ('recusado', 'Recusado'),
            ('cancelado', 'Cancelado'),
            ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='orcamentos')
    lista_de_materiais = models.TextField()
    total_preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_frete = models.CharField(max_length=20, choices=FORMAS_RECEBIMENTO)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='salvo')

    criado_em = models.DateTimeField(default=timezone.now)
    cep_entrega = models.CharField(max_length=10, blank=True, null=True)
    rua = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True) 
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return f'Orçamento {self.pk} - {self.cliente.nome}'

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    unidade_medida = models.CharField(max_length=20)
    def __str__(self):
        return self.nome
    

class ItemOrcamento(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, blank=True)
    nome_produto = models.CharField(max_length=100, blank=True, null=True)
    unidade_medida = models.CharField(max_length=20, blank=True, null=True)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
         nome = ( self.produto.nome 
                 if self.produto 
                 else self.nome_produto or 'Produto removido')
         return f"{self.quantidade} x {nome}"

