from django.db import models
from apps.produtos.models import Produtos

from apps.empresa.models import Empresa
from apps.tax.models import Aliquotas, Tributo

# Create your models here.


class GrupoCustos(models.Model):
    descricao = models.CharField('Descrição do Grupo', max_length=100)
    

    class Meta:
        verbose_name = 'Grupo de Custos'
        verbose_name_plural = 'Grupos de Custos'

    def __str__(self):
        return self.descricao

class SubGrupoCustos(models.Model):
    grupo_custos = models.ForeignKey(GrupoCustos, on_delete=models.CASCADE, related_name='gruposcustos', verbose_name="Grupo de Custos")
    descricao = models.CharField('Descrição do SubGrupo', max_length=150)
    sequencia = models.IntegerField('Sequência Subgrupo')
    

    class Meta:
        verbose_name = 'SubGrupo de Custos'
        verbose_name_plural = 'SubGrupos de Custos'

    def __str__(self):
        return self.descricao

class ItemCustos(models.Model):
    subgrupo_custos = models.ForeignKey(SubGrupoCustos, on_delete=models.CASCADE, related_name='subgruposcustos', verbose_name='SubGrupos Custos')
    descricao = models.CharField('Descrição do Item', max_length=150)
    sequencia = models.IntegerField('Sequência Item')
    

    class Meta:
        verbose_name = 'Item Custo'
        verbose_name_plural = 'Itens Custos'

    def __str__(self):
        return self.descricao


class PrecoItemCustos(models.Model):
    empresas = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='empresas', verbose_name='Empresa')
    item_custos = models.ForeignKey(ItemCustos, on_delete=models.CASCADE, related_name='itens', verbose_name='Itens Custos')
    unidade = models.CharField('Unidade', max_length=150)
    custo_medio = models.DecimalField('Custo Médio', max_digits=10, decimal_places=2)
    ultima_compra = models.DecimalField('Última Compra', max_digits=10, decimal_places=2)
    data_inicio_vigencia = models.DateField('Data de Início da Vigência')
    data_fim_vigencia = models.DateField('Data Final da Vigência')
    ativo = models.BooleanField('Ativo', default=True)
    

    class Meta:
        verbose_name = 'Preço do Item'
        verbose_name_plural = 'Preços dos Itens'

    def __str__(self):
        return str(self.item_custos)

class ProvisaoCustos(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='empresaprovisao', verbose_name='Empresa')
    descricao = models.CharField('Descrição da Provisão', max_length=150)
    valor = models.DecimalField('Valor da Provisão',max_digits=10, decimal_places=2, help_text='Informar o percentual sem o símbolo %')
    

    class Meta:
        verbose_name = 'Provisão'
        verbose_name_plural = 'Provisões'

    def __str__(self):
        return self.descricao

class ItemProdutos(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Empresas", )
    produtos = models.ForeignKey(Produtos, on_delete=models.CASCADE, related_name='itensprodutos', verbose_name="Produtos")
    itens = models.ManyToManyField(PrecoItemCustos, verbose_name='Itens Custos')
    provisoes = models.ManyToManyField(ProvisaoCustos, verbose_name='Provisões', blank=True, null=True)
    tributos = models.ManyToManyField(Aliquotas, verbose_name='Tributos e Encargos', blank=True, null=True)
    class Meta:
        verbose_name = 'Item Produto'
        verbose_name_plural = 'Itens dos Produtos'

    def __str__(self):
        return str(self.produtos)