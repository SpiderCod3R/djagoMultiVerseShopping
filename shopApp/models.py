from django.db import models
from django.utils.translation import gettext_lazy as _


class Base(models.Model):
    criado_em = models.DateField(_('Criação'), auto_now_add=True)
    atualizado_em = models.DateField(_('Atualizado'), auto_now_add=True)
    ativo = models.BooleanField(_('Ativo?'), default=True)

    class Meta:
        abstract = True


class Categoria(Base):
    nome = models.CharField(_('Nome'), max_length=100, unique=True)
    slug = models.CharField(_('Nome na Url'), max_length=100, unique=True)
    descricao = models.TextField(_('Descrição'), max_length=255, blank=True)
    imagem = models.ImageField(_('Imagem'), upload_to='imagens/categorias', blank=True)

    class Meta:
        verbose_name = _('Categoria')
        verbose_name_plural = _('Categorias')

    def __str__(self):
        return self.nome
