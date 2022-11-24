from django.db import models

# Create your models here.


class usuario(models.Model):
    nombre = models.CharField(max_length = 64, default = '')
    apellido = models.CharField(max_length = 64, default = '')
    codigo =  models.CharField(max_length = 64, default = '')
    contraseña = models.CharField(max_length = 64, default = '')
    
class tarea(models.Model):
    titulo = models.CharField(max_length = 128, default = '')
    descripcion = models.CharField(max_length = 256, default = '')
    fechaCreacion = models.CharField(max_length = 32, default = '')
    fechaEntrega = models.CharField(max_length = 32, default = '')
    usuarioDesignado = models.CharField(max_length = 32, default = '')