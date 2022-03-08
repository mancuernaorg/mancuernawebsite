
from . import views
from .views import *
from django.urls import path, include

urlpatterns = [
    path('noticias', views.NoticiasView, name='noticias'),
    path('noticias/<int:pk>', views.NoticiaDetail.as_view(), name='noticia-detalle'), 
    path('bolsaempleo', views.BolsaEmpleo, name='bolsaempleo'),
    path('bolsaempleo/<int:pk>', views.BolsaEmpleoDetail.as_view(), name='bolsa-detalle'),  

]