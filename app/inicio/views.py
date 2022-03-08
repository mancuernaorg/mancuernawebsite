from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def mi_error_404(request, exception):
    return page_not_found(request, '404.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('index') 
    
#Index
class InicioView(generic.TemplateView):
    template_name = 'index.html'
#Bolsa de empleo
class BolsaEmpleoView(generic.TemplateView):
    template_name = 'bolsa_empleo/bolsa_empleo.html'
    #dejar la opcion para varios archivos 
#Noticias


class ContactoView(generic.TemplateView):
    template_name = 'contacto/contacto.html'
#Equipo de trabajo
class EquipoTrabajoView(generic.TemplateView):
    template_name = 'nosotros/equipo-trabajo.html'
#Junta Directiva

class MunicipiosSociosView(generic.TemplateView):
    template_name = 'municipios/municipios_socios.html'
#Sobre nosotros
class SobreNosotrosView(generic.TemplateView):
    template_name = 'nosotros/nuestra_historia.html'

#Informacion Publica


#Programas y componentes
class ProgramaComponentesWiew(generic.TemplateView):
    template_name = 'programas_componentes/programa_componentes.html' 
