from django.contrib import admin

from .models import *

class CategoriaAdmin(admin.ModelAdmin): 
    list_display = (
                    'nombre_categoria',)
admin.site.register(Categoria, CategoriaAdmin) 

class ContenidoAdmin(admin.ModelAdmin): 
    list_display = (
                    'titulo_contenido', 'descripcion', 
                     'enlance', 'cargar_archivo', 'status', 
                    'fecha_publicacion')
admin.site.register(Contenido, ContenidoAdmin) 

 

 