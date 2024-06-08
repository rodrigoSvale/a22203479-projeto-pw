from django.shortcuts import render
from .models import *

def index_view(request):
    aluno = Aluno.objects.all()
    nomes = aluno.values_list('nome')
    rodrigo = aluno.get(numero = 22203479)
    context = {
        'aluno' : aluno,
        'rodrigo' : rodrigo,
        'nomes' : nomes
        }
    return render(request,'teste/index.html',context)


def outro_view(request):
    return render(request,'teste/outro.html')