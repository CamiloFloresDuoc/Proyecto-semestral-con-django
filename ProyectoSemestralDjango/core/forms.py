from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Contacto, Noticias


# se crea clase para el formulario de la base de datos

class NoticiasForm(ModelForm):
    class Meta:
        model = Noticias
        fields = ['titulo', 'cuerpo', 'categoria','imagen']

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre','correo','asunto','mensaje']
