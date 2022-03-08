from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from inicio import views
from django.conf.urls import handler404
from inicio.views import mi_error_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.InicioView.as_view(), name='index'),
    #vistas en desarollo
    #path('contacto', views.ContactoView.as_view(), name='contacto'),
    #path('equipo', views.EquipoTrabajoView.as_view(), name='equipo-trabajo'),
    #path('municipios-socios', views.MunicipiosSociosView.as_view(), name='municipios-socios'),
    #path('sobre-nosotros', views.SobreNosotrosView.as_view(), name='sobre-nosotros'),
    #gestion documentaria ruta que se debe proteger

    path('', include('ejeproyectos.urls')),
    path('', include('infopublic.urls')),
    path('', include('baseconocimiento.urls')),
    path('', include('publicaciones.urls')),
    path('', include('juntadirectiva.urls')),
    path('', include('inicio.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = mi_error_404 