from django.shortcuts import render
from .service import ProdutoService

_SERVICE = ProdutoService()

def home(request):
    return render(request, 'home.html')

def home_produtos(request):
    produtos = _SERVICE.buscar_todos_produtos()
    return render(request, 'home-produtos.html', context={"produtos":produtos})