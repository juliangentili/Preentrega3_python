from django.db import models
# Create your models here.
class Neumatico(models.Model):
    marca = models.CharField(max_length=40)
    ancho = models.IntegerField(null=True,blank=True)
    relacion = models.IntegerField(null=True,blank=True)
    rodado = models.IntegerField()
    valor = models.IntegerField(null=True,blank=True)
    
    def __Str__(self):
        return f"{self.marca} - {self.rodado}"


class Usuario(models.Model):
    email = models.EmailField(default='sin@email.com')
    clave = models.CharField(max_length=40)

class Antirrobo(models.Model):
    marca = models.CharField(max_length=40)
    precio = models.IntegerField()

class clientes(models.Model):   
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)