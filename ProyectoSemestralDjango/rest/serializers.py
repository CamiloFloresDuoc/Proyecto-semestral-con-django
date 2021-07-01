from rest_framework import fields, serializers
from core.models import Noticias

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticias
        fields = ['noticia_id','titulo', 'cuerpo', 'categoria']