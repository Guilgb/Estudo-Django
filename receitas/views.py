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


def pedidos(request):
    template_name = 'pedidos.html'
    carrinho = request.session.get("pedidos_id", None)

    if carrinho is None:
        print('Crie um Carrinho')
        request.session['pedidos_id'] = 12
    else:
        print('Carrino existe')

    def total(request):
        pedidos_obj, new_obj = Pedidos.objects.new_or_get(request)
        comidas = pedidos_obj.comidas.all()
        total = 0
        for comida in comidas:
            total += comida.preco
        print(total)
        pedidos_obj.total = total
        pedidos_obj.save()
    return render(request, template_name, {})


def list_produto(requst):
    template = "pedidos.html"
    pedido = Pedidos.objects.order_by('produtos')
    context = {
        'pedidos': pedido
    }
    print(context)
    return render(requst, template, context)
