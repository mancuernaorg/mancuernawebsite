
from . import views
from .views import *
from django.urls import path, include

urlpatterns = [

    path('junta-directiva', views.JuntaDirectivaView, name='junta-directiva'),

]