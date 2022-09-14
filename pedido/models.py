from django.db import models
from django.contrib.auth.models import User
from receitas.models import Receita

# Create your models here.


class PedidoManager(models.Manager):
    def new_or_get(self, request):
        pedido_id = request.session.get("pedido_id", None)
        qs = self.get_queryset().filter(id=pedido_id)
        if qs.count() == 1:
            new_obj = False
            pedido_obj = qs.first()
            if(request.user.is_authenticated and pedido_obj.user is None):
                pedido_obj.user = request.user
                pedido_obj.save()
        else:
            pedido_obj = Pedidos.objects.new(user=request.user)
            new_obj = True
            request.session['pedido_id'] = pedido_obj.id
        return pedido_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Pedidos(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Receita, blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    obj = PedidoManager()

    def __str__(self) -> str:
        return str(self.id)
