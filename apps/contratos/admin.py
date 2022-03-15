from django.contrib import admin
from apps.contratos.models import Contratos

# Register your models here.

@admin.register(Contratos)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('empresas', 'cod_crs', 'cod_grupo', 'descricao')
    list_filter  = ('empresas', 'descricao')
    search_fields = ('empresas__nome','descricao','cod_grupo', 'cod_crs')
    list_editable = ('cod_crs', 'cod_grupo', 'descricao')
    list_per_page = 10
