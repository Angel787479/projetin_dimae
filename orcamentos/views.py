import json
from django.http import JsonResponse
# Importa a tabela Cliente que desenhamos no arquivo models.py do lado
from .models import Cliente, Produto



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
            'cep': cliente.cep,                   # CEP salvo na gaveta
        })
        
    # Devolve a lista de dados estruturada em formato JSON (texto puro)
    return JsonResponse(lista_para_api, safe=False) 

def atualizar_produto(request, id):
    if request.method != 'PATCH':
        return JsonResponse(
            {'error': 'Método não permitido'}, 
            status=405)
    try:
       produto = Produto.objects.get(id=id)

    except Produto.DoesNotExist:
           
        return JsonResponse(
       {'error': 'Produto não encontrado'}, 
         status=404
      )

    dados = json.loads(request.body)

    if 'nome' in dados:
             produto.nome = dados['nome']
    if 'preco' in dados:
            produto.preco = dados['preco']
    if 'quantidade' in dados:
            produto.quantidade = dados['quantidade']
    produto.save()

    return JsonResponse(
    {
        'id': produto.id,
        'nome': produto.nome,
        'preco': str(produto.preco),
        'quantidade': produto.quantidade
    }
)

def listar_produtos(request):

    categorias = request.GET.getlist('categoria')

    if categorias:

        produtos_do_banco = Produto.objects.filter(categoria__in=categorias)
    else:
        produtos_do_banco = Produto.objects.all()

    lista_para_api = []
    
    for produto in produtos_do_banco:
        lista_para_api.append({
            'id': produto.id,
            'nome': produto.nome,
            'categoria': produto.categoria,
            'descricao': produto.descricao,
            'preco': str(produto.preco),
            'quantidade': produto.quantidade,
            'unidade_medida': produto.unidade_medida
        })
    return JsonResponse(lista_para_api, safe=False)

 
def listar_categorias(request):
    categorias = Produto.objects.values_list('categoria', flat=True).distinct()
    return JsonResponse(list(categorias), safe=False)