from rest_framework import serializers

from.models import *

class ProdutoSerializador(serializers.ModelSerializer):

    class Meta:

        model = Produto

        fields = "__all__"