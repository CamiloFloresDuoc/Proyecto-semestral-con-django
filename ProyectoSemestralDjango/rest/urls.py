from collections import namedtuple
from django.urls import path
from rest.views import detalle_noticia, lista_noticias

urlpatterns = [
    path('noticias', lista_noticias,name="lista_noticias"),
    path('noticias/<id>', detalle_noticia,name='detalle_noticia'),
]