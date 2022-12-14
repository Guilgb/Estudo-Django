from . import views
from django.urls import path


urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('cria/receita', views.cria_receita, name="cria_receita"),
    path('deleta/<int:receita_id>/receita',
         views.deleta_receita, name='deleta_receita'),
    path('edita/<int:receita_id>/receita',
         views.edita_receita, name='edita_receita'),
    path('atualiza_receita', views.atualiza_receita, name='atualiza_receita'),
]
