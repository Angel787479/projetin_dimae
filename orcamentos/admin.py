from django.contrib import admin

# Register your models here.
# Importa a área administrativa do Django
from django.contrib import admin

# Importa as tabelas que criamos no models.py
from .models import Cliente, Orcamento, Produto

# Faz a tabela Cliente aparecer no painel admin
admin.site.register(Cliente)
admin.site.register(Orcamento)
admin.site.register(Produto)