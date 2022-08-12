from django.contrib import admin
from .models import Pessoa

# Register your models here.


class ListarPessoa(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome', 'email')


admin.site.register(Pessoa, ListarPessoa)
