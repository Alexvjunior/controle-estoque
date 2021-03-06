import uuid
from django.shortcuts import redirect, render
from django.contrib import messages
from .service import ProdutoService
from .serializers import ProdutoSerializer

_SERVICE = ProdutoService()

def home(request):
    return render(request, 'home.html')

def home_produtos(request, id:uuid=None):
    if id is not None:
        _SERVICE.deletar_produto_por_id(id)
    elif request.method == "POST" and id is None:
        serializer = ProdutoSerializer(data=request.POST)
        if not serializer.is_valid():
            messages.error(request, serializer.errors)
        else:
            serializer.save()
    produtos = _SERVICE.buscar_todos_produtos()
    return render(request, 'home-produtos.html', context={"produtos":produtos})

def home_editar_produto(request, id:uuid):
    produto = _SERVICE.buscar_produto_por_id(id)
    
    if request.method == "GET":
        return render(request, 'home-editar-produto.html', context={"produto":produto})

    serializer = ProdutoSerializer(produto, request.POST)
    if not serializer.is_valid():
        messages.error(request, serializer.errors)
    else:
        serializer.save()
        messages.success(request, "Salvo com sucesso")
    return render(request, 'home-editar-produto.html', context={"produto":produto})
    
