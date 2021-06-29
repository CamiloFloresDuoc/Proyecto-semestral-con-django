from django.forms.forms import Form
from .forms import NoticiasForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Noticias
from .models import Categoria


def index(request):

    autor = Autor.objects.all()
    noticias = Noticias.objects.all()
    categoria = Categoria.objects.all()

    datos = {
        'noticias' : noticias,
        'autor' : autor,
        'categoria' : categoria
    }
    return render(request, 'core/index.html', datos)

def AboutUs(request):
    return render(request, 'core/AboutUs.html')

def Login(request):
    return render(request, 'core/Login.html')

def news(request):
    return render(request,'core/news.html')

def Register(request):
    return render(request, 'core/Register.html')

def noticias(request):

    autor = Autor.objects.all()
    noticias = Noticias.objects.all()
    categoria = Categoria.objects.all()

    datos = {
        'noticias' : noticias,
        'autor' : autor,
        'categoria' : categoria
    }
    return render(request,'core/noticias.html',datos)

def periodista(request):

    noticias = Noticias.objects.all()

    datos = {
        'noticias' : noticias
    }
    return render(request, 'core/periodista.html',datos)

def nuevaNoticia(request):

    datos = {
        'form' : NoticiasForm()
    }

    if (request.method == 'POST'):
        formulario = NoticiasForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Noticia guardada exitosamente!'
            
           
    return render(request,'core/nuevaNoticia.html',datos)

def editarNoticia(request, noticia_id):

    noticias = get_object_or_404(Noticias, noticia_id=noticia_id)

    datos = {
        'form': NoticiasForm(instance=noticias)
    }

    if request.method == 'POST':
        formulario = NoticiasForm(request.POST, instance=noticias, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Noticia Modificada Correctamente!'
            
        datos["form"] = formulario

    return render(request, 'core/editarNoticia.html',datos)

def eliminarNoticia(request, noticia_id):
    
    noticias = Noticias.objects.get(noticia_id=noticia_id)
    noticias.delete()
    return redirect(to="periodista")
    
    
def notiId(request, noticia_id):

    
    noticias = Noticias.objects.filter(noticia_id=noticia_id)
    

    datos = {
        'noticias' : noticias,
        'noticia_id' : noticia_id,
        
        
    }

    return render(request,'core/notiId.html',datos)
    