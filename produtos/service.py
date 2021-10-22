import uuid

from django.core.exceptions import ValidationError
from .models import ProdutoModel

class ProdutoService():

    def buscar_todos_produtos(self) -> list[ProdutoModel]:
        return ProdutoModel.objects.all()

    def buscar_produto_por_id(self, id:uuid) -> ProdutoModel:
        return ProdutoModel.objects.filter(id=id).first()
    
    def buscar_produto_por_codigo(self, codigo:str) -> ProdutoModel:
        return ProdutoModel.objects.filter(codigo=codigo).first()
    
    def deletar_produto_por_id(self, id:uuid) -> int:
        return ProdutoModel.objects.filter(id=id).delete()

    def editar_produto(self, produto:ProdutoModel, data:dict):
        produto.nome = data.get("nome")
        produto.codigo = data.get("codigo")
        try:
            produto.save()
            return None
        except Exception as e:
            return e.args

