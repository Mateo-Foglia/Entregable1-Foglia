from django.db import models

# Create your models here.

class Juegos(models.Model):
    nombre = models.CharField(max_length=60)
    puntaje = models.FloatField(default=0)

class Libros(models.Model):
    titulo = models.CharField(max_length=60)
    puntaje = models.FloatField(default=0)

class Peliculas(models.Model):
    titulo = models.CharField(max_length=60)
    puntaje = models.FloatField(default=0)
