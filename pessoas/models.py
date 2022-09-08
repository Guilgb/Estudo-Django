from django.db import models

# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    adm = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
