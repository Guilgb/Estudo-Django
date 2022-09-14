from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pedidos
# Register your models here.


class ListaPedidosAdm(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    list_per_page = 30


admin.site.register(Pedidos, ListaPedidosAdm)
