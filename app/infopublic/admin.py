from django.contrib import admin

from .models import *

class CategoriaAdmin(admin.ModelAdmin): 
    list_display = (
                    'categoria',)
admin.site.register(Categoria, CategoriaAdmin) 

class DocumentosAdmin(admin.ModelAdmin): 
    list_display = (
                    'titulo', 'descripcion', 
                     'enlace', 'cargar_archivo', 'status', 
                    'fecha_publicacion')
admin.site.register(Documentos, DocumentosAdmin) 

 