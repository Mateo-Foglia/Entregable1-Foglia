from django.db import models

# Create your models here.

class Juegos(models.Model):

    def __str___(self):
        return f"{self.nombre}"

    nombre = models.CharField(max_length=60)
    puntaje = models.IntegerField(default=1)

class Libros(models.Model):

    def __str___(self):
        return f"{self.nombre}"

    titulo = models.CharField(max_length=60)
    puntaje = models.IntegerField(default=1)

class Peliculas(models.Model):

    def __str___(self):
        return f"{self.nombre}"

    titulo = models.CharField(max_length=60)
    puntaje = models.IntegerField(default=1)
