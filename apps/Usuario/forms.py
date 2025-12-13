from django import forms
from .models import Usuario

class registroform(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nome_usuario', 'email', 'senha', 'imagem']

    def clean(self):
        cleaned = super().clean()
        s1 = cleaned.get('senha')
        s2 = cleaned.get('senha_confirm')
        if s1 and s2 and s1 != s2:
            raise forms.ValidationError('As senhas não coincidem.')
        return cleaned