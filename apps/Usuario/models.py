from django.db import models

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.nome_usuario
