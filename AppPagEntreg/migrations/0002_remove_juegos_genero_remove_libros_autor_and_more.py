# Generated by Django 4.1.1 on 2022-09-23 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPagEntreg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juegos',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='libros',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='libros',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='peliculas',
            name='duracion',
        ),
        migrations.RemoveField(
            model_name='peliculas',
            name='genero',
        ),
        migrations.AddField(
            model_name='juegos',
            name='puntaje',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='libros',
            name='puntaje',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='puntaje',
            field=models.FloatField(default=0),
        ),
    ]