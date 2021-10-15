import uuid
from .models import ProdutoModel

class ProdutoService():

    def buscar_todos_produtos(self) -> list[ProdutoModel]:
        return ProdutoModel.objects.all()

    def buscar_produto_por_id(self, id:uuid) -> ProdutoModel:
        return ProdutoModel.objects.filter(id=id).first()
    
    def buscar_produto_por_codigo(self, codigo:str) -> ProdutoModel:
        return ProdutoModel.objects.filter(codigo=codigo).first()