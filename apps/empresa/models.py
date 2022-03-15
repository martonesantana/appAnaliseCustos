from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField('Nome da Empresa', max_length=100)
    razaosocial = models.CharField('Razão Social', max_length=200)
    cnpj = models.CharField('CNPJ', max_length=18, unique=True)
    codigoERP = models.CharField('Código ERP', max_length=10,)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome