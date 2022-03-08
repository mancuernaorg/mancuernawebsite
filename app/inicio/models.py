from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class Usuario(AbstractUser):

    ROLES = [
        (0, "Administrador"),
        (1, "Tecnico"),
        (2, "Colaborador"),
        (3, "Admin de base de conocimientos"),
        (4, "Editor de Base de conocimientos"), 
    ]
    rol = models.PositiveSmallIntegerField(choices=ROLES)

    # Campos requeridos
    REQUIRED_FIELDS = ['password','first_name', 'last_name', 'rol', 'email']



