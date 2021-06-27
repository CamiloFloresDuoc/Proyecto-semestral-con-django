from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, IntegerField
from django.db.models.fields.files import ImageField

# Create your models here.
# Modelo para la categoria

class Categoria(models.Model):
    Categoria = models.IntegerField(primary_key=True, verbose_name='Id Categoria')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria

# Modelo para autor

class Autor(models.Model):
    Autor = models.IntegerField(primary_key=True, verbose_name= 'Id Autor')
    nombreAutor = models.CharField(max_length=100,verbose_name='Nombre Autor')

    def __str__(self):
        return self.nombreAutor

class Noticias(models.Model):
    noticia_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100,verbose_name='Titulo Noticia')
    cuerpo = models.TextField(max_length=1000,verbose_name='Cuerpo Noticia')
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)
    imagen = models.ImageField(upload_to="images")

    def __str__(self):
        return self.titulo

