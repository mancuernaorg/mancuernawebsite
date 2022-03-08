from django.db import models

#Junta directiva
class JuntaDirectiva(models.Model):
    nombre_representante = models.CharField(max_length=200) 
    fotografia = models.ImageField(upload_to='juntad')
    DIRECTIVA = [
        (0, ""),
        (1, "PRESIDENTE"),
        (2, "VICE PRESIDENTE"),
        (3, "SECRETARIA"),
        (4, "TESORERA"),
        (5, "VOCAL 1"),
        (6, "VOCAL 2"),
        (7, "VOCAL 3"),
    ]
    electivo = models.DateField(auto_now_add=False)
    puesto = models.IntegerField(choices=DIRECTIVA, null=False, blank=False, default=0)
    STATUS = [
        (0, "Publicado"),
        (1, "Ocultar"),
    ]
    status = models.IntegerField(choices=STATUS, default=0)
    fecha_publicacion =  models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name = "Junta Directiva"
  