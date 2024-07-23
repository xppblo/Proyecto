from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    romanNumber = models.CharField(max_length=50, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)
    
    def __str__(self):
        return f" {self.name}"

class Comuna(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    region = models.ForeignKey(Region, null=False, blank=False, on_delete= models.CASCADE)
    
    def __str__(self):
        return f" {self.nombre}"
    
class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=20, null=False, blank=False)
     
    def __str__(self):
        return f"{self.id} - {self.nombre}"
    
class Usuario(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete= models.CASCADE)
    rut = models.CharField(unique=True)
    telefono = models.CharField(max_length=15, blank=False, null=False)
    tipo_usuario = models.ForeignKey(TipoUsuario, null=False, blank=False, on_delete= models.CASCADE)
    
    def __str__(self):
        return f"{self.id} - {self.user.first_name} {self.user.last_name}"
    
class TipoInmueble(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return f"{self.nombre}"
    
class Inmueble(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=255, null=False, blank=False)
    depto = models.CharField(max_length=20, blank=True)
    m2_construidos = models.FloatField(null=False, blank=False)
    m2_totales = models.FloatField(null=False, blank=False)
    estacionamientos = models.IntegerField(null=False, blank=False)
    habitaciones = models.IntegerField(null=False, blank=False)
    banios = models.IntegerField(null=False, blank=False)
    precio = models.FloatField(null=False, blank=False)
    arrendado = models.BooleanField(null=False, default=False)
    tipo_inmueble = models.ForeignKey(TipoInmueble, null=False, blank=False, on_delete= models.CASCADE)
    region = models.ForeignKey(Region, null=False, blank=False, on_delete= models.CASCADE)
    comuna = models.ForeignKey(Comuna, null=False, blank=False, on_delete= models.CASCADE)
    usuarios = models.ManyToManyField(Usuario, related_name='inmuebles')
    
    def __str__(self):
        return f"{self.id} - {self.nombre}"