import uuid
from django.shortcuts import render
from rest_framework import serializers
from django.contrib import messages
from .service import ProdutoService
from .serializers import ProdutoSerializer
from django.http import HttpResponseRedirect

_SERVICE = ProdutoService()

def home(request):
    return render(request, 'home.html')

def home_produtos(request, id:uuid=None):
    if request.method == "POST" and id is not None:
        _SERVICE.deletar_produto_por_id(id)
    produtos = _SERVICE.buscar_todos_produtos()
    return render(request, 'home-produtos.html', context={"produtos":produtos})

def home_editar_produto(request, id:uuid):
    produto = _SERVICE.buscar_produto_por_id(id)

    if request.method == "GET":
        return render(request, 'home-editar-produto.html', context={"produto":produto})

    message = _SERVICE.editar_produto(produto, request.POST)
    if message is not None:
        messages.error(request, message)
        messages.warning(request, "ERROR")
        messages.info(request, "INFO")
        return render(request, template_name='home-editar-produto.html', context={"produto":produto})
    messages.success(request, "Salvo com sucesso")
    return render(request, 'home-editar-produto.html', context={"produto":produto})
    # return HttpResponseRedirect("/produtos/")
    