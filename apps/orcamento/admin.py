from django.contrib import admin

from apps.orcamento.models import Orcamento

# Register your models here.

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('empresas', 'cod_contrato', 'cod_contabil', 'data', 'valor', 'versao', 'movimento')
    list_filter  = ('empresas', 'cod_contrato', 'cod_contabil')
    search_fields = ['empresas__nome', 'cod_contrato__descricao','cod_contabil__descricao']
    list_per_page = 10