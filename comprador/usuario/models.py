# Importações do Django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .manages import UsuarioManager



# Modelo do Usuario
class Usuario(AbstractBaseUser, PermissionsMixin):

    # Dados de acesso e permissão
    email = models.EmailField(_('E-mail'), unique=True, max_length=255)
    nome_usuario = models.CharField(_('Nome do Usuario'), max_length=255)
    password = models.CharField(_("Senha"), max_length=255)
    is_staff = models.BooleanField(_("Administrador?"), default=False)
    is_active = models.BooleanField(_("Ativo?"), default=True)
    is_trusty = models.BooleanField(_('Verificado?'), default=True)
    date_joined = models.DateTimeField(_("Criação"), default=timezone.now)

    # Campo de autenticação
    USERNAME_FIELD = 'email'

    # Gerenciador de operações de criação
    objects = UsuarioManager()

    # Retorno padrão do objeto da classe
    def __str__(self):
        return self.email

    # Nome da tabela no Banco de Dados
    class Meta:
        db_table="usuario"