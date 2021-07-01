from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import Serializer
from core.views import noticias
from rest.serializers import NoticiaSerializer
from django.shortcuts import render
from core.models import Noticias
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
@api_view(['GET','POST'])

def lista_noticias(request):
    if request.method == 'GET':
        noticias = Noticias.objects.all()
        serializer = NoticiaSerializer(noticias,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoticiaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])

def detalle_noticia(request,id):
    try:
        noticias = Noticias.objects.get(noticia_id=id)
    except Noticias.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Serializer = NoticiaSerializer(noticias)
        return Response(Serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        Serializer = NoticiaSerializer(noticias,data=data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data)
        else:
            return Response(Serializer.error,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        noticias.delete()
        return Response(status.HTTP_204_NO_CONTENT)
