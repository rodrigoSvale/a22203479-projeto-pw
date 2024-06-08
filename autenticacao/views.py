from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate, login, logout

def register_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('autenticacao:login')

    return render(request, 'autenticacao/register.html')


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
        request,
        username = request.POST['username'],
        password = request.POST['password'])

        if user is not None:
            login(request, user)
            return render(request, 'autenticacao/user.html')
        else:
            render(request,'autenticacao/login.html',{'mensagem':'Credenciais inválidas'})

    return render(request,'autenticacao/login.html')

def logout_view(request):
    logout(request)
    return redirect('autenticacao:login')