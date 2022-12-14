from django.urls import path
from AppPagEntreg.views import *
from django.contrib.auth.views import LogoutView

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
    path('login/', inicioSesion, name="Login"),
    path('register/', registro, name="SignUp"),
    path('logout/', LogoutView.as_view(template_name="AppPagEntreg/20_logout.html"), name="Logout"),
    path('editarUsuario/', editarUsuario, name="Editar Usuario"),

    #CRUD (salvo por la "C" que está en los distintos "add.."):
    #READ:
    path('leerPelis/', leerPelis, name="Ver todas las películas"),
    path('leerLibros/', leerLibros, name="Ver todos los libros"),
    path('leerJuegos/', leerJuegos, name="Ver todos los juegos"),

    #DELETE:
    path('eliminarPelis/<peliTitulo>/', eliminarPelis, name="Eliminar películas"),
    path('eliminarLibros/<libroTitulo>/', eliminarLibros, name="Eliminar libros"),
    path('eliminarJuegos/<juegoNombre>/', eliminarJuegos, name="Eliminar juegos"),

    #UPDATE:
    path('editarPelis/<peliTitulo>/', modificarPelis, name="Editar películas"),
    path('editarLibros/<libroTitulo>/', modificarLibros, name="Editar libros"),
    path('editarJuegos/<juegoNombre>/', modificarJuegos, name="Editar juegos"),
]
