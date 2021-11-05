from django.contrib import admin
from .models import Categoria, SubCategoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('fc', 'fm')
    list_display = ["descripcion", "estado", "fc", "fm", "uc", "um"]
    list_editable = ['estado']
    search_fields = ['descripcion', 'uc', 'um']
    list_filter = ['estado']
    list_per_page = 8

@admin.register(SubCategoria)
class SubCategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('fc', 'fm')
    list_display = ["descripcion", "estado", "fc", "fm", "uc", "um"]
    list_editable = ['estado']
    search_fields = ['descripcion', 'uc', 'um']
    list_filter = ['estado']
    list_per_page = 8
