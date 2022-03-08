from django.db import models

# Create your models here.
class Eje(models.Model):
    nombre_eje = models.CharField(max_length=200) 

    def __str__(self):
        return self.nombre_eje    
    class Meta:
        verbose_name = "Ejes" 
        verbose_name_plural = "Ejes" 

class Cooperante(models.Model):
    nombre_cooperante = models.CharField(max_length=200) 

    def __str__(self):
        return self.nombre_cooperante  
    class Meta:
        verbose_name = "Nombre del cooperante" 

class LugarEjecucion(models.Model):
    nombre_lugar = models.CharField(max_length=200) 

    def __str__(self):
        return self.nombre_lugar
    class Meta:
        verbose_name = "Lugar de ejecución"
        verbose_name_plural = "Lugar de ejecución"  

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200) 
    descripcion = models.CharField(max_length=200) 
    imagen_principal = models.ImageField(upload_to='noticias_imagenes')
    eje = models.ForeignKey(Eje, on_delete= models.CASCADE,related_name='eje', null=False, blank=False)
    cooperante = models.ForeignKey(Cooperante, on_delete= models.CASCADE,related_name='coperante', null=False, blank=False)
    lugar_ejecucion  = models.ForeignKey(LugarEjecucion, on_delete= models.CASCADE,related_name='ejecucion', null=False, blank=False)
    AVANCESPROYECTO = [
        (0, ""),
        (1, "Iniciado"),
        (2, "En progreso"),
        (3, "Finalizado"),
    ]
    avances_proyecto = models.IntegerField(choices=AVANCESPROYECTO, default=0)
    STATUS = [
        (0, "Publicado"),
        (1, "Ocultar"),
    ]
    status = models.IntegerField(choices=STATUS, default=0)
    fecha_publicacion =  models.DateTimeField(auto_now_add=True) 
    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = "Publicación de proyectos"
  
class PostGaleryImage(models.Model):
    post = models.ForeignKey(Proyecto, default=None, on_delete=models.CASCADE)
    imagenes= models.FileField(upload_to = 'proyectos/')
    class Meta:    
        verbose_name = "Fotografias"