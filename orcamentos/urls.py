
from unittest.mock import patch
from django.urls import path
from . import views  # Puxa o arquivo views.py que está na mesma pasta

urlpatterns = [
    # Quando o link principal for acessado, ele ativa a função de ler o banco
    path('', views.home, name='home'),
    path('produtos/',
        views.listar_produtos,
        name='listar_produtos'),    
    path(
         'categorias/',
        views.listar_categorias,
        name='listar_categorias'
        ),
]