from django import forms
from .models import Usuario
from pixelzone.utils import verify_password

class UsuarioRegisterForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, label='Senha')
    senha_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirmar senha')

    class Meta:
        model = Usuario
        fields = ['nome_usuario', 'email', 'senha']

    def clean(self):
        cleaned = super().clean()
        s1 = cleaned.get('senha')
        s2 = cleaned.get('senha_confirm')
        if s1 and s2 and s1 != s2:
            raise forms.ValidationError('As senhas não coincidem.')
        return cleaned

class UsuarioLoginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)