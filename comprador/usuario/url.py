from django.urls import path

# Importações do Sistema
from .views import *


urlpatterns = [

    # usuário URLs
    path('',UsuarioListar.as_view(), name='listar-usuario'),
    path('<int:pk>/',UsuarioDetalhar.as_view(), name='detalhar-usuario'),
    path('cadastrar/',UsuarioCadastrar.as_view(), name='cadastrar-usuario'),
    path('atualizar/<int:pk>/',UsuarioAtualizar.as_view(), name='atualizar-usuario'),
    path('deletar/<int:pk>/',UsuarioDeletar.as_view(), name='deletar-usuario'),


]