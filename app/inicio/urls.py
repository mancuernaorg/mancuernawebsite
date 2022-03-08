
   
from . import views
from .views import *
from django.urls import path, include

urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')),
    path('logout', views.logout_view, name='logout'),
]

