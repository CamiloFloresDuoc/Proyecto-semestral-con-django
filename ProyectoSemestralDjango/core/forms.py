from django import forms
from django.forms import ModelForm
from .models import Noticias


# se crea clase para el formulario de la base de datos

class NoticiasForm(ModelForm):
    class Meta:
        model = Noticias
        fields = ['titulo', 'cuerpo', 'categoria','imagen']