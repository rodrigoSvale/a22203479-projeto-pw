from django.shortcuts import render

def landing_page(request):
    return render(request, 'Portfolio/landing_page.html')

def about(request):
    return render(request, 'Portfolio/about.html')

def aboutsite(request):
    return render(request, 'Portfolio/aboutsite.html')

def contacto(request):
    return render(request, 'Portfolio/contacto.html')

def projetos(request):
    return render(request, 'Portfolio/projetos.html')

