from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.empresa.models import Empresa

# Create your models here.


class PlanoDeContas(models.Model):

    natureza_choices = [
        ('C', 'Credora'),
        ('D', 'Devedora'),
    ]

    empresas = models.ForeignKey(Empresa, on_delete=models.CASCADE,
                                 related_name='empresas_contabilidade', verbose_name='Empresa')
    codigo = models.CharField(
        'Código', max_length=14, help_text='Informe o código do plano de contas do ERP')
    descricao = models.CharField('Descrição', max_length=155)
    reduzido = models.CharField(
        'Reduzido', max_length=3, blank=True, null=True)
    analitica = models.BooleanField('Analítica', default=False)
    patrimonial = models.BooleanField('Patrimonial', default=False)
    natureza = models.CharField(
        'Natureza', max_length=1, choices=natureza_choices)
    seq = models.PositiveIntegerField('Seq', blank=True, null=True)

    class Meta:
        verbose_name = 'Plano de Contas'
        verbose_name_plural = 'Plano de Contas'

    def __str__(self):
        return self.descricao

class Fechamento(models.Model):
    ano = models.PositiveIntegerField('Ano', validators=[MinValueValidator(2022), MaxValueValidator(2030)])
    jan = models.BooleanField('Janeiro', default=False)
    fev = models.BooleanField('Fevereiro', default=False)
    mar = models.BooleanField('Março', default=False)
    abr = models.BooleanField('Abril', default=False)
    mai = models.BooleanField('Maio', default=False)
    jun = models.BooleanField('Junho', default=False)
    jul = models.BooleanField('Julho', default=False)
    ago = models.BooleanField('Agosto', default=False)
    set = models.BooleanField('Setembro', default=False)
    out = models.BooleanField('Outubro', default=False)
    nov = models.BooleanField('Novembro', default=False)
    dez = models.BooleanField('Dezembro', default=False)

    class Meta:
        verbose_name = 'Fechamento'
        verbose_name_plural = 'Fechamento'
    
    def __str__(self):
        return str(self.ano)

