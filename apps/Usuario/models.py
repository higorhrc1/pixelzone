from django.db import models

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='usuario/', blank=True, null=True, default='usuario/default.png')
    def __str__(self):
        return self.nome_usuario
