from django.db import models
from django.contrib.auth.models import User

class registro(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    nombredeusuario = models.CharField()
    contraseña = models.CharField()
    trabajo = models.CharField()

    
class productos(models.Model):
    nombre_producto = models.CharField(max_length= 40)
    descripcion_producto = models.CharField()
    categoria = models.CharField(max_length=30)
    precio = models.IntegerField()
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    usuario_creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productos_subidos')

    def __str__(self):
        return self.nombre
    
class avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Campo obligatorio por defecto
    imagen = models.ImageField(upload_to='avatares/', null=True, blank=True) # Si la imagen es opcional
    
    def __str__(self):
        return f"Avatar de {self.user.username}"

# Create your models here.
