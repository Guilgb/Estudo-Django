from django.shortcuts import render, redirect
from receitas.models import Receita
from pedido.models import Pedidos

# Create your views here.


def pedidos(self, request):
    pedido_obj = Pedidos.obj.new_or_get(request)
    produtos = pedido_obj.produtos.all()
    total = 0
    for receita in produtos:
        total += receita.preco
    print(total)
    pedido_obj.total = total
    pedido_obj.save()
    return render(request, "pedidos.html", {})


def pedidos_update(request):
    receita_id = 1
    receita_obj = Receita.objects.get(id=receita_id)

    pedido_obj, new_obj = Pedidos.objects.new_oor_get(request)
    pedido_obj.receita.add(receita_obj)
    return redirect(receita_obj.get_absolute_url())
