from django.urls import path
from . import views

app_name = 'jogos'

urlpatterns = [
    path('', views.lista_jogos, name='lista'),
    path('<int:pk>/', views.detalhe_jogo, name='detalhe'),
    path('criar/', views.criar_jogo, name='criar'),
    path('editar/<int:pk>/', views.editar_jogo, name='editar'),
    path('excluir/<int:pk>/', views.excluir_jogo, name='excluir'),
    path('favorito/<int:pk>/', views.adicionar_favorito, name='favorito'),
]