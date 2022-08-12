from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def cadastro(request):
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if(not nome.strip() or not email.strip() or not senha.strip()
           or not senha2.strip() and senha != senha2):
            print('Verifique os campos')
            return redirect('cadastro')

        if(User.objects.filter(email=email).exists()):
            print('Ususario já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(
            username=nome, email=email, password=senha)
        user.save()
        print('Cadastrado')
        return redirect('login')
    else:
        return render(request, 'users/cadastro.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print("Dados invalidos")
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list(
                'username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'users/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'users/dashboard.html')
    else:
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')
