from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Material(models.Model):
    idMaterial = models.AutoField(primary_key=True, verbose_name='Id de material')
    nombreMaterial = models.CharField(max_length=50, verbose_name='Nombre de material')
    descripcionMaterial = models.CharField(max_length=50, verbose_name='Descripcion de material')
    stock = models.IntegerField(verbose_name='Stock de material')

    def __str__(self):
        return self.nombreMaterial

class Taller(models.Model):
    idTaller = models.AutoField(primary_key=True, verbose_name='Id de taller')
    nomTaller = models.CharField(max_length=50, null=True,blank=True, verbose_name='Nombre de taller')
    descripcionTaller = models.CharField(max_length=50, verbose_name='Descripcion de taller')
    sala = models.IntegerField(verbose_name='Sala de taller')
    fechaInicio = models.CharField(max_length=50, verbose_name='Fecha inicio')
    fechaTermino = models.CharField(max_length=50, verbose_name='Fecha termino')
    instructor = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

    def nombreTaller(self):
        return self.nombreTaller


class PostulacionInstr(models.Model):
    idPostulacion = models.AutoField(primary_key=True, verbose_name='Id de postulacion')
    nombres = models.CharField(max_length=50, verbose_name='Nombre de postulante')
    apellidos = models.CharField(max_length=50, verbose_name='Apellido de postulante')
    correo = models.CharField(max_length=50, verbose_name='Correo de postulante')
    direccion = models.CharField(max_length=50, verbose_name='Direccion de postulante')
    rut = models.CharField(max_length=50, verbose_name='rut de postulante')
    estado = models.CharField(max_length=50, verbose_name='estado de postulante',default="Pendiente")
    taller = models.CharField(max_length=50, verbose_name='Nombre de taller')
    descripcion = models.CharField(max_length=100, verbose_name='Breve descripción del taller')
    
    def __str__(self):
        return self.nombresci



class Instructor(models.Model):
    idInstructor = models.AutoField(primary_key=True, verbose_name='Id de instructor')
    nombres = models.CharField(max_length=50, verbose_name='Nombre de instructor')
    apellidos = models.CharField(max_length=50, verbose_name='Apellido de instructor')
    correo = models.CharField(max_length=50, verbose_name='Correo de instructor')
    direccion = models.CharField(max_length=50, verbose_name='Direccion de instructor')
    rut = models.CharField(max_length=50, verbose_name='rut de instructor')
    estado = models.CharField(max_length=50, verbose_name='estado de instructor')

    def __str__(self):
        return self.nombres
