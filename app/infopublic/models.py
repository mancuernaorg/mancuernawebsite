from django.db import models
class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria    
    class Meta:
        verbose_name = "Nombre de la categoria" 

class Documentos(models.Model):
    titulo = models.CharField(max_length=200) 
    descripcion = models.CharField(max_length=200) 
    enlace = models.CharField(max_length=200,blank=True,null=True) 
    cargar_archivo = models.FileField(upload_to="infopublica/",blank=True,null=True)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE,related_name='categoriainfopublic', null=False, blank=False)
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
        verbose_name = "Información Pública"
  