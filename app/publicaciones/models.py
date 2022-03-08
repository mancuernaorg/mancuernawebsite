#seccion de noticias, bolsa de empleo
from django.db import models

class Noticia(models.Model):
    titulo_noticia = models.CharField(max_length=200) 
    imagen_principal = models.ImageField(upload_to='noticias_imagenes')
    descripcion = models.CharField(max_length=1000) 
    enlace = models.CharField(max_length=200,blank=True,null=True) 
    CATEGORIA = [
        (0, "Noticias"),
        (1, "Información Pública"),
    ]
    categoria = models.IntegerField(choices=CATEGORIA, default=0) 
    STATUS = [
        (0, "Publicado"),
        (1, "Ocultar"),
    ]
    status = models.IntegerField(choices=STATUS, default=0)
    fecha_publicacion =  models.DateTimeField(auto_now_add=True) 
    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo_noticia
    class Meta:
        verbose_name = "Noticia"


class BolsaDeEmpleo(models.Model):
    titulo = models.CharField(max_length=200) 
    cargar_archivo = models.FileField(upload_to="media/",blank=True,null=True)
    descripcion = models.CharField(max_length=200) 
    STATUS = [
        (0, "Publicado"),
        (1, "Ocultar"),
    ]
    status = models.IntegerField(choices=STATUS, default=0)
    fecha_publicacion =  models.DateTimeField(auto_now_add=True) 
    class Meta:
        ordering = ['fecha_publicacion']

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = "Bolsa de empleo y TDRS"
        