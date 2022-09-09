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

    def __str__(self):
        return self.nome_receita


class Pedidos(models.Model):
    comida = models.ForeignKey(
        Receita, on_delete=models.CASCADE, related_name='pedidos')
    preco_total = models.DecimalField(max_digits=4, decimal_places=2)
