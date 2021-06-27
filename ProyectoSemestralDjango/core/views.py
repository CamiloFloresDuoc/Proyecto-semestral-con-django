from .forms import NoticiasForm
from django.shortcuts import render
from .models import Noticias
from .models import Categoria

def index(request):
    return render(request, 'core/index.html')

def AboutUs(request):
    return render(request, 'core/AboutUs.html')

def Login(request):
    return render(request, 'core/Login.html')

def news(request):
    return render(request,'core/news.html')

def Register(request):
    return render(request, 'core/Register.html')

def noticias(request):

    noticias = Noticias.objects.all()

    datos = {
        'noticias' : noticias
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

    if request.method == 'POST':
        formulario = NoticiasForm(request.POST, request.FILES)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Noticia guardado exitosamente'

    return render(request,'core/nuevaNoticia.html',datos)