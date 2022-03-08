from django.shortcuts import render
from django.views import generic
from .models import Documentos, Categoria
from django.views import generic
from django.core.paginator import Paginator

class InformacionPublicaView(generic.ListView):
    #listar y categorias
    template_name = 'informacion/informacion_publica.html'
    paginate_by = 10 #paginacion de documentos
    def get_queryset(self):
        qs = Documentos.objects.filter(status=0)  
        categoria = self.request.GET.get('categoria', None)
        if categoria:
            qs = qs.filter(Q(categoria__categoria=categoria))
        return qs

    def get_context_data(self, **kwargs):
        context = super(InformacionPublicaView, self).get_context_data(**kwargs)
        context.update({
            "categorias": Categoria.objects.all()
        })
        return context