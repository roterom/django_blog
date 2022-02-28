from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion')
    resource_class = CategoriaResource


class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor    
    
class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', 'apellidos', 'correo']
    list_display = ('nombre', 'apellidos', 'correo', 'estado', 'fecha_creacion')
    resource_class = AutorResource


# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)