from django.shortcuts import render
from django.views import generic
from .models import Contenido, Categoria
from django.views import generic
from django.db.models import Q

class BaseDeConocimientoView(generic.ListView):
    #listar y categorias
    template_name = 'base_conocimiento/base_conocimiento.html' 
    paginate_by = 10 #paginacion de documentos
    def get_queryset(self):
        qs = Contenido.objects.filter(status=0)
        categoria = self.request.GET.get('categoria', None)
        if categoria:
            qs = qs.filter(Q(categoria__nombre_categoria=categoria))
        return qs

    def get_context_data(self, **kwargs):
        context = super(BaseDeConocimientoView, self).get_context_data(**kwargs)
        context.update({
            "categorias": Categoria.objects.all()
        })
        return context