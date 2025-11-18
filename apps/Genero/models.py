from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
