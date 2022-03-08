from django.shortcuts import render
from django.views import generic
from .models import JuntaDirectiva
from django.views import generic
from django.core.paginator import Paginator
# Create your views here.


def JuntaDirectivaView(request):
    directiva = JuntaDirectiva.objects.all()
    paginator = Paginator(directiva,6) 
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'junta_directiva/juntadirectiva.html', context={'directiva': directiva, 'directiva': page_obj} )



