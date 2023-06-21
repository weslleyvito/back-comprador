from django.db import models
from django.utils.translation import gettext_lazy as _

class Produto(models.Model):

    nome_produto = models.CharField(_("Nome do Produto"), max_length=255)
    preco_produto = models.DecimalField(_("Preço do Produto"), max_digits=4, decimal_places=2)
    medida_produto = models.DecimalField(_("Medida de Produto"), max_digits=4, decimal_places=2)

    def __str__(self):
        return self.nome_produto

    # Nome da tabela no Banco de Dados
    class Meta:
        db_table="listacompras"