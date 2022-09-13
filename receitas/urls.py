from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar'),
    path('pedido/', views.pedidos, name='pedidos'),
    path('pedido/lista/', views.list_produto, name='pedidos_list')
]
