from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Receita(models.Model):
    nome_receita = models.CharField(max_length=255)
    ingredientes = models.TextField()
    modo_de_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    foto_receita = models.ImageField(
        upload_to='fotos/%d/%m/%Y', blank='True')
    preco = models.DecimalField(max_digits=4, decimal_places=2)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome_receita


class Pedidos(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Receita, blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.produtos}'


class GerentePedidos(models.Manager):
    def new_or_get(self, request):
        pedidos_id = request.session.get("pedidos_id")
        qs = self.get_queryset().filter(id=pedidos_id)

        if qs.count() == 1:
            new_obj = False
            pedidos_obj = qs.first()

            if request.users.is_authenticated is None:
                pedidos_obj.user = request.user
                pedidos_obj.save()
            else:
                pedidos_obj = Pedidos.objects.new(user=request.user)
                new_obj = True
                request.session['pedidos_id'] = pedidos_obj.id
            return pedidos_obj, new_obj

    def new(self, user=None):
        user_obj = None

        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)
