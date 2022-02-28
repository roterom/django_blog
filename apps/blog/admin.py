from django.contrib import admin
from .models import *


class CategoriaAdmin(admin.ModelAdmin):
    
    search_fields = ['nombre']
    list_display = ('nombre', 'estado', 'fecha_creacion')
    
    
class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellidos', 'correo']
    list_display = ('nombre', 'apellidos', 'correo', 'estado', 'fecha_creacion')

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)