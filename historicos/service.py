from .models import HistoricoModel
from produtos.service import ProdutoService

_SERVICE_PRODUTO = ProdutoService()

class HistoricoService():

    def salvar_historico(self, data:dict):
        produto = _SERVICE_PRODUTO.buscar_produto_por_id(data.get("produto_id"))
        historico = HistoricoModel(
            produto_id=produto,
            funcionario=data.get("funcionario"),
            tipo=data.get("tipo"),
            descricao=data.get("descricao"),
            quantidade=data.get("quantidade"),
        )
        historico.save()

    def buscar_todos_historicos(self):
        return HistoricoModel.objects.all()