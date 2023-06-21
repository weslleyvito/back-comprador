from django.urls import path

from .views import *

# Importações do Sistema
from .views import *


urlpatterns = [

    # produto URLs
    path('',ProdutoListar.as_view(), name='listar-produto'),
    path('<int:pk>/',ProdutoDetalhar.as_view(), name='detalhar-produto'),
    path('cadastrar/',ProdutoCadastrar.as_view(), name='cadastrar-produto'),
    path('atualizar/<int:pk>/',ProdutoAtualizar.as_view(), name='atualizar-produto'),
    path('deletar/<int:pk>/',ProdutoDeletar.as_view(), name='deletar-produto'),


]