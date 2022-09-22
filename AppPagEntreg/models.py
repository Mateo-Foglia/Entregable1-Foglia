from django.db import models

# Create your models here.

class Juegos(models.Model):
    nombre = models.CharField(max_length=60)
    genero = models.CharField(max_length=60)

class Libros(models.Model):
    titulo = models.CharField(max_length=60)
    autor = models.CharField(max_length=60)
    genero = models.CharField(max_length=60)

class Peliculas(models.Model):
    titulo = models.CharField(max_length=60)
    duracion = models.FloatField()
    genero = models.CharField(max_length=60)
