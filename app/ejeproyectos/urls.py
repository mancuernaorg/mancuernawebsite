
from . import views
from .views import *
from django.urls import path, include

urlpatterns = [

    path('proyectos', views.ProyectosView, name='proyectos'),

]