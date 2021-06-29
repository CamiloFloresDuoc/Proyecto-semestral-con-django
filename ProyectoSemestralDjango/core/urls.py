from django.urls import path
from .views import AboutUs, Login, Register, index, news, noticias, periodista, nuevaNoticia, editarNoticia, eliminarNoticia, notiId

urlpatterns = [
    path('',index,name="index"),
    path('AboutUs/',AboutUs, name="AboutUs"),
    path('Login/', Login, name="Login"),
    path('news/', news, name="news"),
    path('Register/', Register, name="Register"),
    path('noticias/',noticias,name="noticias"),
    path('periodista/',periodista,name="periodista"),
    path('nuevaNoticia/',nuevaNoticia,name="nuevaNoticia"),
    path('editarNoticia/<noticia_id>/',editarNoticia,name="editarNoticia"),
    path('eliminarNoticia/<noticia_id>/',eliminarNoticia,name="eliminarNoticia"),
    path('notiId/<noticia_id>/',notiId,name="notiId"),
    
]