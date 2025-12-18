from django import forms
from .models import Usuario

class registroform(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nome_usuario', 'email', 'senha', 'imagem']
        widgets = {'senha': forms.PasswordInput()}