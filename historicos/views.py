from re import I
from django.shortcuts import render
from rest_framework import serializers
from produtos.service import ProdutoService
from .serializers import HistoricoSerializer
from django.contrib import messages
from .service import HistoricoService

_SERVICE_PRODUTO = ProdutoService()
_SERVICE = HistoricoService()

def home_historico(request):
    if request.POST:
        serializer = HistoricoSerializer(data=request.POST)
        if not serializer.is_valid():
            messages.error(request, serializer.errors)
        else:
            _SERVICE.salvar_historico(request.POST)
    produtos = _SERVICE_PRODUTO.buscar_todos_produtos()
    historicos = _SERVICE.buscar_todos_historicos()
    return render(request, 'home_historico.html', context={"produtos":produtos, "historicos":historicos})