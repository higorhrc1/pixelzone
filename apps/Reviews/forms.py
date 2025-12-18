from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['nota', 'comentario']
        widgets = {'comentario': forms.Textarea(attrs={'rows':4})}
        widgets = {'nota': forms.NumberInput(attrs={'min':1,'max':10})}
