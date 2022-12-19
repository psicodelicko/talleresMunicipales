from django.db import models

# Create your models here.


class Material(models.Model):
    idMaterial = models.AutoField(primary_key=True, verbose_name='Id de material')
    nombreMaterial = models.CharField(max_length=50, verbose_name='Nombre de material')
    descripcionMaterial = models.CharField(max_length=50, verbose_name='Descripcion de material')
    stock = models.IntegerField(verbose_name='Stock de material')

    def __str__(self):
        return self.nombreMaterial


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
