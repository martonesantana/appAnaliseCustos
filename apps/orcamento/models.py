from django.db import models
from apps.contabilidade.models import PlanoDeContas
from apps.empresa.models import Empresa
from apps.contratos.models import Contratos

# Create your models here.


class Orcamento(models.Model):

    mvto_choices = [
        ('1', '1'),
        ('-1', '-1'),
    ]
    
    empresas = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='orcamento_empresas', verbose_name='Empresa')
    cod_contrato = models.ForeignKey(Contratos, on_delete=models.CASCADE, related_name='orcamento_contratos', verbose_name='Contrato do Orçamento')
    cod_contabil = models.ForeignKey(PlanoDeContas, on_delete=models.CASCADE, related_name='orcamento_contabil', verbose_name='Conta Contábil do Orçamento')
    data = models.DateField('Data da Competência', help_text='Informe a data de competência')
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    versao = models.CharField('Versão', max_length=10, null=True, blank=True)
    movimento = models.CharField('Movimento', max_length=2, choices=mvto_choices)
    
    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'

    def __str__(self):
        return str(self.cod_contabil)
