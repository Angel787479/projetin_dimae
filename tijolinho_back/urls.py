from django.contrib import admin
from django.urls import path, include  # Puxa o 'include' para conseguir chamar o filho

urlpatterns = [
    path('admin/', admin.site.urls),  # Caminho padrão do painel do Django
    
    # Avisa o projeto que o aplicativo 'orcamentos' agora controla a página inicial
    path('', include('orcamentos.urls')),
]
