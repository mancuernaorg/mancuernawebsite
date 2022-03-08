from django.contrib import admin

from .models import *

class NoticiaAdmin(admin.ModelAdmin): 
    list_display = (
                    'titulo_noticia', 'descripcion', 
                     'enlace', 'categoria', 'status', 
                    'fecha_publicacion')
admin.site.register(Noticia, NoticiaAdmin) 


class BolsaDeEmpleoAdmin(admin.ModelAdmin): 
    list_display = (
                    'titulo', 'descripcion', 
                    'status', 'fecha_publicacion')
admin.site.register(BolsaDeEmpleo, BolsaDeEmpleoAdmin) 