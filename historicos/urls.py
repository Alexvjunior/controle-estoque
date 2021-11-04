from django.urls import path
from .views import home_historico

namespace = 'hitoricos'

urlpatterns = [
    path('historicos', home_historico, name="home_historicos"),
]
