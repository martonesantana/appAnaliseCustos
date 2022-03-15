from django.contrib import admin

from apps.contabilidade.models import PlanoDeContas, Fechamento
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter)

# Register your models here.


@admin.register(PlanoDeContas)
class PlanoDeContasAdmin(admin.ModelAdmin):
    list_display = ('empresas', 'codigo', 'descricao',
                    'reduzido', 'analitica', 'patrimonial', 'natureza')
    list_filter = ('empresas__nome', 'descricao')
    list_editable = ('codigo', 'descricao', 'reduzido',
                     'analitica', 'patrimonial', 'natureza')
    search_fields = ('empresas__nome', 'codigo', 'descricao',
                     'reduzido', 'analitica', 'patrimonial', 'natureza')
    list_per_page = 10
    fieldsets = (
        (None, {
            "fields": [('empresas'), ('codigo', 'reduzido'), ('descricao'), ('analitica'), ('patrimonial'), ('natureza', 'seq')

                       ],
        }),
    )

@admin.register(Fechamento)
class FechamentoAdmin(admin.ModelAdmin):
    list_display = ('ano', 'jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')
    list_editable = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')
    list_per_page = 10
    fieldsets = (
        (None, {
            "fields": [('ano'), ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')
                       ],
        }),
    )