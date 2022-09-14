from .views import (
    pedidos_update,
    pedidos,
)
from django.urls import path


urlpatterns = [
    path("home_pedido", pedidos, name='pedido'),
    path("pedido_update", pedidos_update, name='update_pedido')
]
