from django.shortcuts import render

def home_historico(request):
    return render(request, 'home_historico.html')