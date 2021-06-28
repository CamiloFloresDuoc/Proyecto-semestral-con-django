from django.contrib import admin
from .models import Autor, Categoria, Noticias, Contacto

# Register your models here.
# Permite administrr el modelo completo

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Noticias)
admin.site.register(Contacto)
