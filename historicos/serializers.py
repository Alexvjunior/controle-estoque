from .models import HistoricoModel
from rest_framework import serializers
from produtos.service import ProdutoService

_SERVICE_PRODUTO = ProdutoService()

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoModel
        fields = ('id', 'produto_id', 'funcionario', 'tipo', 'descricao')