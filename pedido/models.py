from django.db import models
from django.contrib.auth.models import User
from receitas.models import Receita
from django.db.models.signals import pre_save, post_save, m2m_changed

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
    subtotal = models.DecimalField(
        default=0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    objects = PedidoManager()

    def __str__(self) -> str:
        return str(self.id)


def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if (action == 'post_add' or action == 'post_remove' or
            action == 'post_clear'):
        products = instance.produtos.all()
        total = 0
        for product in products:
            total += product.preco
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()


m2m_changed.connect(m2m_changed_cart_receiver, sender=Pedidos.produtos.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        # considere o 10 como uma taxa de entrega
        instance.total = Decimal(instance.subtotal) * Decimal(1.80)
    else:
        instance.total = 0.00


pre_save.connect(pre_save_cart_receiver, sender=Pedidos)
