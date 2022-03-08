from django.shortcuts import render
from django.views import generic
from .models import *
from django.views import generic
from django.core.paginator import Paginator



def ProyectosView(request):    
    proyectos = Proyecto.objects.all()
    paginator = Paginator(proyectos,4)
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'proyectos/proyectos.html', 
                    context={'proyectos': proyectos, 
                            'proyectos': page_obj,
                            
                            })


