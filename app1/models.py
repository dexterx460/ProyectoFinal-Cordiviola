from django.db import models

class registrarse(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
class blog(models.Model):
    titulo = models.CharField(max_length= 40)
    descripcion = models.CharField()
    subtitulo = models.CharField(max_length= 50)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
class productos(models.Model):
    nombre_producto = models.CharField(max_length= 40)
    descripcion_producto = models.CharField()
    categoria = models.CharField(max_length=30)
    
class buscar(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)

# Create your models here.
