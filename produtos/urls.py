from django.urls import path
from .views import home

namespace = 'produtos'

urlpatterns = [
    path('', home, name="home"),
]
