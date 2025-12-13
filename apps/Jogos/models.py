from django.db import models
from apps.Genero.models import Genero

class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    plataforma = models.CharField(max_length=50)
    data_lancamento = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='jogos')
    imagem = models.ImageField(upload_to='jogos/')
    def __str__(self):
        return self.nome
