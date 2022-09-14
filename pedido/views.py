from django.shortcuts import render, redirect
from receitas.models import Receita
from pedido.models import Pedidos

# Create your views here.


def pedidos(request):
    pedido_obj, new_obj = Pedidos.objects.new_or_get(request)
    return render(request, "pedidos.html", {"pedidos": pedido_obj})


def pedidos_update(request):
    print(request.POST)
    receita_id = request.POST.get('receita_id')
    if receita_id is not None:
        try:
            receita_obj = Receita.objects.get(id=receita_id)
        except Receita.DoesNotExist:
            print('Esse produto não esta mais em estoque')
            return redirect("pedido:home_pedido")
        pedido_obj, new_obj = Pedidos.objects.new_or_get(request)
        if receita_obj in pedido_obj.produtos.all():
            pedido_obj.produtos.remove(pedido_obj)
        else:
            pedido_obj.produtos.add(receita_obj)
        request.session['pedido_items'] = pedido_obj.produtos.count()
    return redirect("pedido")
