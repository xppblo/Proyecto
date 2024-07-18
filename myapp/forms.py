from django import forms
from .models import *
from django_select2 import forms as s2forms

class UsuarioForm(forms.ModelForm):
    #rut = forms.CharField(label='Rut')
    telefono = forms.CharField(label='Teléfono')
    
    class Meta:
        model = Usuario
        fields = ['telefono']