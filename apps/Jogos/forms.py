from django import forms
from .models import Jogo
from apps.Genero.models import Genero

class JogoForm(forms.ModelForm):
    data_lancamento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Jogo
        fields = ['nome', 'descricao', 'plataforma', 'data_lancamento', 'genero', 'imagem']
