from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('register/', views.registro, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),

    
    path('lista/', views.lista_usuarios, name='lista'),
    path('editar/<int:pk>/', views.editar_usuario, name='editar'),
    path('excluir/<int:pk>/', views.excluir_usuario, name='excluir'),
]