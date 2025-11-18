from django.db import models
from apps.Usuario.models import Usuario
from apps.Jogos.models import Jogo

class Review(models.Model):
    nota = models.IntegerField()
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='reviews')
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"{self.usuario.nome_usuario} - {self.jogo.nome} ({self.nota}/10)"
