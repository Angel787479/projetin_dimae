from django.http import JsonResponse
# Importa a tabela Cliente que desenhamos no arquivo models.py do lado
from .models import Cliente

def listar_clientes(request):
    # O comando que vai no banco de dados e busca TODOS os clientes cadastrados
    clientes_do_banco = Cliente.objects.all()
    
    # Criamos uma lista em branco no Python para organizar as informações
    lista_para_api = []
    
    # Passamos de linha em linha na tabela do banco, pegando os dados de cada um
    for cliente in clientes_do_banco:
        lista_para_api.append({
            'id': cliente.id,                     # Número do cadastro automático
            'nome': cliente.nome,                 # Nome salvo na gaveta
            'whatsapp': cliente.whatsapp,         # Celular salvo na gaveta
            'endereco': cliente.endereco_padrao,  # Endereço salvo na gaveta
        })
        
    # Devolve a lista de dados estruturada em formato JSON (texto puro)
    return JsonResponse(lista_para_api, safe=False)
