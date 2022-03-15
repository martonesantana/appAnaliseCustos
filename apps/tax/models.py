from django.db import models

from apps.empresa.models import Empresa

# Create your models here.


class CategoriaTributo(models.Model):
    descricao = models.CharField('Descrição da Categoria', max_length=150)

    class Meta:
        verbose_name = 'Categoria dos Tributos'
        verbose_name_plural = 'Categorias dos Tributos'

    def __str__(self):
        return self.descricao


class Tributo(models.Model):
    CategoriaTributo = models.ForeignKey(CategoriaTributo,
                                         on_delete=models.CASCADE,
                                         related_name='categoriatributos',
                                         verbose_name="Categoria dos Tributos")
    descricao = models.CharField('Descrição do Tributo', max_length=150)

    class Meta:
        verbose_name = 'Tributo'
        verbose_name_plural = 'Tributos'

    def __str__(self):
        return self.descricao


class Aliquotas(models.Model):
    empresa = models.ForeignKey(Empresa,
                                on_delete=models.CASCADE,
                                related_name='empresa',
                                verbose_name="Empresa")

    tributo = models.ForeignKey(Tributo,
                                on_delete=models.CASCADE,
                                related_name='tributos',
                                verbose_name="Tributo")
    aliquota = models.DecimalField(
        'Alíquota',
        max_digits=10,
        decimal_places=2,
        help_text='Informar o percentual sem o símbolo %')

    class Meta:
        verbose_name = 'Alíquota'
        verbose_name_plural = 'Alíquotas'

    def __str__(self):
        return str(self.tributo)