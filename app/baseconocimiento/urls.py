from . import views
from .views import *
from django.urls import path, include

urlpatterns = [

    path('base-conocimiento', views.BaseDeConocimientoView.as_view(), name='base-conocimiento'),
]

