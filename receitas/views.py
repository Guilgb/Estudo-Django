from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Pedidos, Receita
from django.views.decorators.csrf import requires_csrf_token

# Create your views here.


def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receita.html', receita_a_exibir)


@requires_csrf_token
def buscar(request):
    lista_receitas = Receita.objects.order_by(
        '-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_busca = request.GET['buscar']

        if buscar:
            lista_receitas = lista_receitas.filter(
                nome_receita__icontains=nome_busca)

    lista_dados = {
        'receitas': lista_receitas
    }
    return render(request, 'buscar.html', lista_dados)


def pedidos(request, pedido_id):
    template_name = 'pedidos.html'
    carrinho = Pedidos.objects.filter(pk=pedido_id)

    context = {'object_list': carrinho, }

    return render(request, template_name, context)
