from django.shortcuts import render, redirect
from receitas.models import Pedidos, Receita

# Create your views here.


def pedidos(request):
    key = request.session.session_key
    print(key)
    return render(request, "pedidos.html")


def pedidos_update(request):
    receita_id = 1
    receita_obj = Receita.objects.get(id=receita_id)

    pedido_obj, new_obj = Pedidos.objects.new_oor_get(request)
    pedido_obj.receita.add(receita_obj)
    return redirect(receita_obj.get_absolute_url())
