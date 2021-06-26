from django.shortcuts import render

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
    return render(request,'core/noticias.html')

def periodista(request):
    return render(request, 'core/periodista.html')