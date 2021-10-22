from django.urls import path
from .views import home, home_produtos, home_editar_produto

namespace = 'produtos'

urlpatterns = [
    path('', home, name="home"),
    path('produtos/', home_produtos, name="home_produtos"),
    path('produtos/<uuid:id>/', home_produtos, name="deletar_produtos"),
    path('produtos/editar/<uuid:id>/', home_editar_produto, name="home_editar_produto"),
]
