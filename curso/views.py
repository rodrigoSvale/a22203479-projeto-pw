from django.shortcuts import render, get_object_or_404
from .models import *

def curso_view(request):
    context = {
        'cursos' : Curso.objects.all(),
    }

    return render (request, 'curso/index.html', context)

def disciplinas_view(request, disciplina_id):
    context = {

        'disciplinas' : Disciplina.objects.all(),
        'disciplina' : Disciplina.objects.get(id = disciplina_id)
    }

    return render(request, 'curso/disciplinas.html', context)


def disciplina_view(request, disciplina_id):
    context = {

        'disciplina' : Disciplina.objects.get(id = disciplina_id)
    }

    return render(request, 'curso/disciplina.html', context)

def projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    context = {
        'projeto': projeto
    }
    return render(request, 'curso/projeto.html', context)