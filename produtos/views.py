from django.shortcuts import render
from .service import ProdutoService

_SERVICE = ProdutoService()

def home(request):
    # produtos = _SERVICE.buscar_todos_produtos()
    return render(request, 'home.html', context={"produtos":produtos})