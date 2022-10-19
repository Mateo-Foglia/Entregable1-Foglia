from django.urls import path
from AppPagEntreg.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('addJuego/', addJuego, name="Añadir juegos"),
    path('addLibro/', addLibro, name="Añadir libros"),
    path('addPeli/', addPeli, name="Añadir películas"),
    path('getJuego/', getJuego, name="Buscar juegos"),
    path('getLibro/', getLibro, name="Buscar libros"),
    path('getPeli/', getPeli, name="Buscar películas"),
    path('buscarLibro/', buscarLibro),
    path('buscarJuego/', buscarJuego),
    path('buscarPeli/', buscarPeli),
    path('leerTodo/', leerTodo),
]
