from . import views
from .views import *
from django.urls import path, include

urlpatterns = [
    #path('informacion-publica', views.InformacionPublicaView.as_view(), name='informacion-publica'),
    path('informacion-publica', views.InformacionPublicaView.as_view(), name='informacion-publica'),
]