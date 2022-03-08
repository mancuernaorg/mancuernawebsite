from django.shortcuts import render
from django.views import generic
from .models import *
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def NoticiasIdexView(request):    
    noticia = Noticia.objects.order_by('?').first()
    paginator = Paginator(relacionadas,4)
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', 
                    context={'noticia': noticia, 
                            'noticia': page_obj,
                            
                            })

def NoticiasView(request):    
    noticia = Noticia.objects.filter(status=0)  
    relacionadas = Noticia.objects.order_by('?').first()
    paginator = Paginator(relacionadas,5)
    paginator = Paginator(noticia,10)
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'noticias/noticias.html', 
                    context={'noticia': noticia, 
                            'noticia': page_obj, 
                            'relacionadas': relacionadas, 
                            'relacionadas': page_obj,
                            
                            })

def BolsaEmpleo(request):
    bolsadeempleo = BolsaDeEmpleo.objects.order_by('-fecha_publicacion')
    paginator = Paginator(bolsadeempleo,20)
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bolsa_empleo/bolsa_empleo.html', context={'bolsadeempleo': bolsadeempleo, 'bolsadeempleo': page_obj})


class BolsaEmpleoDetail(generic.DetailView):
    model = BolsaDeEmpleo
    template_name = 'bolsa_empleo/bolsa_empleo_detalle.html'

class NoticiaDetail(generic.DetailView):
    model = Noticia
    template_name = 'noticias/noticias_detalle.html' 