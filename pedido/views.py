from django.shortcuts import render, redirect
from receitas.models import Receita
from pedido.models import Pedidos

# Create your views here.


def pedidos(request):
    pedido_obj, new_obj = Pedidos.objects.new_or_get(request)
    return render(request, "pedidos.html", {"pedido": pedido_obj})


def pedidos_update(request):
    receita_id = 1
    receita_obj = Receita.objects.get(id=receita_id)

    pedido_obj, new_obj = Pedidos.objects.new_or_get(request)
    pedido_obj.receita.add(receita_obj)
    return redirect(receita_obj.get_absolute_url())
