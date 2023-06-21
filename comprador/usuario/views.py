from .models import Usuario
from .serializer import UsuarioSerializador
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Usuario Listar
class UsuarioListar(generics.ListAPIView):

    # permission_classes = (IsAuthenticated,)

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializador


# Usuario Detalhar
class UsuarioDetalhar(generics.RetrieveAPIView):

    # permission_classes = (IsAuthenticated,)

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializador


# Usuario Cadastrar
class UsuarioCadastrar(generics.CreateAPIView):

    # permission_classes = (IsAuthenticated,)

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializador


# Usuario Atualizar
class UsuarioAtualizar(generics.RetrieveUpdateAPIView):

    # permission_classes = (IsAuthenticated,)

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializador


# Usuario Deletar
class UsuarioDeletar(generics.RetrieveDestroyAPIView):

    # permission_classes = (IsAuthenticated,)

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializador
