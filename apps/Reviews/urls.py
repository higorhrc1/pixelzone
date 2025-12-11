from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('<int:jogo_pk>/', views.lista_reviews, name='lista'),               
    path('criar/<int:jogo_pk>/', views.criar_review, name='criar'),         
    path('editar/<int:pk>/', views.editar_review, name='editar'),           
    path('excluir/<int:pk>/', views.excluir_review, name='excluir'),        
]
