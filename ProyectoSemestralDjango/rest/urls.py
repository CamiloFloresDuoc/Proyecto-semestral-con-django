from collections import namedtuple
from django.urls import path
from rest.views import detalle_noticia, lista_noticias
from rest.viewslogin import login

urlpatterns = [
    path('noticias', lista_noticias,name="lista_noticias"),
    path('noticias/<id>', detalle_noticia,name='detalle_noticia'),
    path('login',login, name="login"),
]