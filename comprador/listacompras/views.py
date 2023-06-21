from .models import Produto
from .serializer import ProdutoSerializador
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Produto Listar
class ProdutoListar(generics.ListAPIView):

    # permission_classes = (IsAuthenticated,)

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializador


# Produto Detalhar
class ProdutoDetalhar(generics.RetrieveAPIView):


    # permission_classes = (IsAuthenticated,)

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializador


# Produto Cadastrar
class ProdutoCadastrar(generics.CreateAPIView):

    permission_classes = ()
    authentication_classes = ()
    # permission_classes = (IsAuthenticated,)

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializador


# Produto Atualizar
class ProdutoAtualizar(generics.RetrieveUpdateAPIView):

    permission_classes = ()
    authentication_classes = ()

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializador


# Produto Deletar
class ProdutoDeletar(generics.RetrieveDestroyAPIView):

    permission_classes = ()
    authentication_classes = ()
    # permission_classes = (IsAuthenticated,)

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializador

