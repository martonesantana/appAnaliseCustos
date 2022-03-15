from django.contrib import admin
from apps.custos.models import GrupoCustos, ItemProdutos, PrecoItemCustos, SubGrupoCustos, ItemCustos, ProvisaoCustos

# Register your models here.

@admin.register(GrupoCustos)
class GrupoCustosAdmin(admin.ModelAdmin):
    list_display = ('descricao',)

@admin.register(SubGrupoCustos)
class SubGrupoCustosAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'grupo_custos', 'sequencia')
    list_editable = ('grupo_custos', 'sequencia')
    list_per_page = 10

@admin.register(ItemCustos)
class ItemCustosAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'subgrupo_custos', 'sequencia')
    list_filter = ('subgrupo_custos',)
    list_editable = ('subgrupo_custos', 'sequencia')
    search_fields = ('descricao',)
    list_per_page = 10
    
@admin.register(PrecoItemCustos)
class ItemCustosAdmin(admin.ModelAdmin):
    list_display = ('empresas','item_custos', 'unidade', 'custo_medio', 'ultima_compra','data_inicio_vigencia', 'data_fim_vigencia', 'ativo')
    list_editable = ('item_custos', 'unidade', 'custo_medio', 'ultima_compra','data_inicio_vigencia', 'data_fim_vigencia', 'ativo')
    search_fields = ('unidade','item_custos',)
    list_per_page = 10

@admin.register(ProvisaoCustos)
class ProvisaoCustosAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'descricao', 'valor')
    list_editable = ('descricao', 'valor')
    list_per_page = 10
    
@admin.register(ItemProdutos)
class ItemProdutosAdmin(admin.ModelAdmin):
    #fields = ['produtos', 'provisoes', 'beneficios', 'tributos', 'itens']
    list_display = ('empresa','produtos', 'Provisoes')
    search_fields = ('produtos',)
    list_per_page = 10
    
    def Provisoes(self, obj):
        return "\n".join([str(p) for p in obj.provisoes.all()])
    
