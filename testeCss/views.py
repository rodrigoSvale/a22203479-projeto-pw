from django.shortcuts import render

def pagina_view(request):
    return render(request,'testeCss/pagina.html')