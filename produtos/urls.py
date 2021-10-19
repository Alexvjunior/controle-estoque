from django.urls import path
from .views import home, home_produtos

namespace = 'produtos'

urlpatterns = [
    path('', home, name="home"),
    path('produtos/', home_produtos, name="home_produtos"),
]
