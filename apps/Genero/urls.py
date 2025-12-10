from django.urls import path
from . import views

app_name = 'genero'

urlpatterns = [
    path('', views.lista_generos, name='lista'),
    path('criar/', views.criar_genero, name='criar'),
    path('editar/<int:pk>/', views.editar_genero, name='editar'),
    path('excluir/<int:pk>/', views.excluir_genero, name='excluir'),
]