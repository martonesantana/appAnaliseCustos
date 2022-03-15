from django.contrib import admin

from apps.produtos.models import GrupoProduto, Produtos

# Register your models here.

@admin.register(GrupoProduto)
class GrupoProdutosAdmin(admin.ModelAdmin):
    list_display = ('descricao',)

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('grupo_produtos', 'descricao')