from rest_framework import serializers

from.models import *

class UsuarioSerializador(serializers.ModelSerializer):

    class Meta:

        model = Usuario

        fields = ["id", "email", "password", "nome_usuario"]