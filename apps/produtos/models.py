from django.db import models

# Create your models here.

class GrupoProduto(models.Model):
    descricao = models.CharField('Grupo dos Produtos', max_length=100)
    

    class Meta:
        verbose_name = 'Grupo de Produtos'
        verbose_name_plural = 'Grupos de Produtos'

    def __str__(self):
        return self.descricao

class Produtos(models.Model):
    grupo_produtos = models.ForeignKey(GrupoProduto, on_delete=models.CASCADE, related_name='gruposprodutos', verbose_name="Grupo dos Produtos")
    descricao = models.CharField('Descrição do Produto', max_length=150)
    
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.descricao