from django.contrib import admin

from apps.empresa.models import Empresa

# Register your models here.

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('codigoERP', 'nome', 'razaosocial', 'cnpj')
    list_editable = ('nome', 'razaosocial', 'cnpj')
    search_fields = ('nome',)