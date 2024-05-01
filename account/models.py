from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_docente = models.BooleanField('Is docente', default=False)
    is_funcionario = models.BooleanField('Is funcionario', default=False)




class Semestre(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre





class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    semestres = models.ManyToManyField(Semestre)

    def __str__(self):
        return self.nombre





class Unidad(models.Model):
        nombre = models.CharField(max_length=100)
        materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

        def __str__(self):
            return self.nombre

class Contenido(models.Model):
        nombre = models.CharField(max_length=100)
        unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)

        def __str__(self):
            return self.nombre

class Clase(models.Model):
        carrera = models.CharField(max_length=100)
        curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
        semestre=models.ForeignKey(Semestre, on_delete=models.CASCADE)
        materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
        unidades = models.ManyToManyField(Unidad, related_name='clases', blank=True)
        contenidos = models.ManyToManyField(Contenido, related_name='clases', blank=True)
        numero_clase = models.IntegerField()
        numero_clase = models.IntegerField()
        fecha = models.DateField()
        hora_inicio = models.TimeField()
        hora_fin = models.TimeField()
        TIPO_CLASE_CHOICES = [
            ('Teorica', 'Teorica'),
            ('Practica', 'Practica'),
            ('Laboratorio', 'Laboratorio'),
        ]
        tipo_clase = models.CharField(max_length=20, choices=TIPO_CLASE_CHOICES)
        numero_alumno = models.IntegerField()
        metodologia=models.TextField(blank=True, null=True)


        def __str__(self):
            return f"{self.materia} - Clase {self.numero_clase} - {self.fecha}"