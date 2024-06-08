# pwsite/views.py

from django.shortcuts import render

def historia_view(request):
    return render(request, "novaapp/historia.html")

def index_view(request):
    return render(request, "novaapp/index.html")

def sobre_view(request):
    return render(request, "novaapp/sobre.html")