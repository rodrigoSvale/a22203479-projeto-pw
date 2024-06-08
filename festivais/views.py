from django.shortcuts import render, get_object_or_404
from .models import *

def index_view(request):
    localizacoes = Localizacao.objects.all()
    context = {
        'localizacoes': localizacoes,
    }
    return render(request, "festivais/festivais.html", context)

def festival_detail_view(request, festival_id):
    festival = get_object_or_404(Festival, id=festival_id)
    context = {
        'festival': festival,
    }
    return render(request, "festivais/festival.html", context)