from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'usuario'

urlpatterns = [
    path('', views.registro, name='registrar'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),   
    path('excluir/<int:pk>/', views.excluir_usuario, name='excluir_usuario'),   
    path('editar/<int:pk>/', views.editar_usuario, name='editar'),
    path('lista/', views.lista, name='lista'),
]