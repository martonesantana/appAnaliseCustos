from django.contrib import admin

from apps.tax.models import Aliquotas, CategoriaTributo, Tributo

# Register your models here.


@admin.register(CategoriaTributo)
class CategoriaTributoAdmin(admin.ModelAdmin):
    list_display = ('descricao', )


@admin.register(Tributo)
class TributoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'CategoriaTributo')

@admin.register(Aliquotas)
class AliquotaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'tributo', 'aliquota')