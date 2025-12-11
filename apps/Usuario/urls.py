from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.registro, name='register'),
    path('login/', views.login, name='login'),

    
    path('lista/', views.lista, name='lista'),
]