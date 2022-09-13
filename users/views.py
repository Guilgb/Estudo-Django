from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from receitas.models import Receita


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
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)

        dados = {
            'receitas': receitas
        }
        return render(request, 'users/dashboard.html', dados)
    else:
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')


def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_de_preparo = request.POST['modo_de_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        preco = request.POST['preco']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa=user,
                                         nome_receita=nome_receita,
                                         ingredientes=ingredientes,
                                         modo_de_preparo=modo_de_preparo,
                                         tempo_preparo=tempo_preparo,
                                         rendimento=rendimento,
                                         categoria=categoria,
                                         foto_receita=foto_receita,
                                         preco=preco)

        receita.save()

        return redirect('dashboard')
    else:
        return render(request, 'users/cria_receita.html')


def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')


def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {'receita': receita}
    return render(request, 'users/edita_receita.html', receita_a_editar)


def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_de_preparo = request.POST['modo_de_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.categoria = request.POST['categoria']
        r.data_receita = request.POST['data_receita']
        r. publicada = request.POST['publicada']
        r.preco = request.POST['preco']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        r.save()
    return redirect('dashboard')
