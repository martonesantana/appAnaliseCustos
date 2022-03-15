from django.db import models
from apps.empresa.models import Empresa

# Create your models here.

class Contratos(models.Model):
    
    empresas = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='empresas_contratos', verbose_name='Empresa')
    cod_crs = models.CharField('Cod Centro Resultado',max_length=100, help_text='Informe o código do ERP referente ao contrato')
    cod_grupo = models.CharField('Cod Grupo',max_length=100, help_text='Informe o código de agrupamento')
    descricao = models.CharField('Nome do Contrato', max_length=100)
    
    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'

    def __str__(self):
        return self.descricao