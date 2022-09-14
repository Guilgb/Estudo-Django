from django.db import models
from django.contrib.auth.models import User
from receitas.models import Receita

# Create your models here.


class Pedidos(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Receita, blank=True)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

