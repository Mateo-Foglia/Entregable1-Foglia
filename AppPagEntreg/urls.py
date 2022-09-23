from django.urls import path
from AppPagEntreg.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('formularioAdd/', addJuego, name="Añadir juegos"),
    path('formularioAdd/', addLibro, name="Añadir libros"),
    path('formularioAdd/', addPeli, name="Añadir películas"),
    path('formularioGet', getJuego, name="Buscar juegos"),
    path('formularioGet', getLibro, name="Buscar libros"),
    path('formularioGet', getPeli, name="Buscar películas"),
]
