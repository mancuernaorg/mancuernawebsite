from django.contrib import admin

from .models import *

admin.site.site_header = 'Sitio Web MANCUERNA' 

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
admin.site.register(Usuario, UsuarioAdmin)