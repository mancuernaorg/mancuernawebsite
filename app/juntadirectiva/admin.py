from django.contrib import admin

from .models import *

class JuntaDirectivaAdmin(admin.ModelAdmin): 
    list_display = (
                    'nombre_representante', 
                     'fotografia', 'status', 
                    'fecha_publicacion')
admin.site.register(JuntaDirectiva,JuntaDirectivaAdmin) 

