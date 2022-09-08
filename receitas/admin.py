from django.contrib import admin
from .models import Receita, Pedidos

# Register your models here.


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria',
                    'tempo_preparo', 'publicada')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita', 'categoria')
    list_filter = ('categoria', 'tempo_preparo')
    list_per_page = 30
    list_editable = ('publicada',)


admin.site.register(Receita, ListandoReceitas)


class ListandoPedidos(admin.ModelAdmin):
    list_display = ('id', )
    list_display_links = ('id', )


admin.site.register(Pedidos, ListandoPedidos)
