from django.contrib import admin

from .models import *

class GaleryImageAdmin(admin.StackedInline):
    model = PostGaleryImage

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    inlines = [GaleryImageAdmin]

    class Meta:
       model = Proyecto
       
class GaleryImageAdmin(admin.ModelAdmin):
    pass

class EjesAdmin(admin.ModelAdmin): 
    list_display = (
                    'nombre_eje', )
admin.site.register(Eje, EjesAdmin) 

class Cooperantedmin(admin.ModelAdmin): 
    list_display = (
                    'nombre_cooperante', )
admin.site.register(Cooperante, Cooperantedmin) 

class LugarEjecucionadmin(admin.ModelAdmin): 
    list_display = (
                    'nombre_lugar', )
admin.site.register(LugarEjecucion, LugarEjecucionadmin) 