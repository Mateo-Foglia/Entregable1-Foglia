from django.shortcuts import render
from django.http import HttpResponse
from AppPagEntreg.models import *
from AppPagEntreg.forms import *

# Create your views here.

def inicio(request):
    return render(request, "AppPagEntreg/2_Inicio.html")

#__________________________________________________________________________________________________________________________________________________________________________________________________________

# Funciones que permiten agregar datos




def addLibro(request):

      if request.method == 'POST':

            miFormulario = FormularioLibros(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  libro = Libros(titulo=informacion['Título'], puntaje=informacion['Puntaje']) 

                  libro.save()

                  return render(request, "AppPagEntreg/2_Inicio.html")

      else: 

            miFormulario= FormularioLibros()

      return render(request, "AppPagEntreg/3_addLibro.html", {"miFormulario":miFormulario})




def addJuego(request):

      if request.method == 'POST':

            miFormulario = FormularioJuegos(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  juego = Juegos(nombre=informacion['Nombre'], puntaje=informacion['Puntaje']) 

                  juego.save()

                  return render(request, "AppPagEntreg/2_Inicio.html")

      else: 

            miFormulario= FormularioJuegos()

      return render(request, "AppPagEntreg/5_addJuego.html", {"miFormulario":miFormulario})




def addPeli(request):

      if request.method == 'POST':

            miFormulario = FormularioPeliculas(request.POST)

            print(miFormulario)

            if miFormulario.is_valid():

                  informacion = miFormulario.cleaned_data

                  pelis = Peliculas(titulo=informacion['Título'], puntaje=informacion['Puntaje']) 

                  pelis.save()

                  return render(request, "AppPagEntreg/2_Inicio.html")

      else: 

            miFormulario= FormularioPeliculas()

      return render(request, "AppPagEntreg/4_addPeli.html", {"miFormulario":miFormulario})


#__________________________________________________________________________________________________________________________________________________________________________________________________________

#Funciones que permiten buscar datos




def getLibro(request):

    return render(request, "AppPagEntreg/6_getLibro.html")


def buscarLibro(request):
    
    if request.GET["Título"]:
        
        titulo = request.GET["Título"]
        libros = Libros.objects.filter(titulo__icontains=titulo)
        
        return render(request, "AppPagEntreg/9_resultadosLibros.html", {"libros":libros, "titulo":titulo})
    
    else:

        respuesta = "Tenés que ingresar datos."

        return HttpResponse(respuesta)




def getJuego(request):

    return render(request, "AppPagEntreg/8_getJuego.html")


def buscarJuego(request):

      if request.GET["Nombre"]:

            nombre = request.GET["Nombre"]
            juegos = Juegos.objects.filter(nombre__icontains=nombre)

            return render(request, "AppPagEntreg/10_resultadosJuegos.html", {"juegos":juegos, "nombre":nombre})

      else:

            respuesta = "Tenés que ingresar datos."

            return HttpResponse(respuesta)





def getPeli(request):

    return render(request, "AppPagEntreg/7_getPeli.html")


def buscarPeli(request):

      if request.GET["Título"]:

            titulo = request.GET["Título"]
            pelis = Peliculas.objects.filter(titulo__icontains=titulo)

            return render(request, "AppPagEntreg/11_resultadosPelículas.html", {"pelis":pelis, "titulo":titulo})

      else:

            respuesta = "Tenés que ingresar datos."

            return HttpResponse(respuesta)

#____________________________________________________________________________________________________________________________________
#Funciones que permiten ver todos los libros/películas/juegos en una sola lista.

def leerPelis(request):

      pelis = Peliculas.objects.all()

      contexto = {"pelis":pelis}

      return render(request, "AppPagEntreg/12_leerPelis.html", contexto)


def leerLibros(request):

      libros = Libros.objects.all()

      contexto = {"libros":libros}

      return render(request, "AppPagEntreg/13_leerLibros.html", contexto)


def leerJuegos(request):

      juegos = Juegos.objects.all()

      contexto = {"juegos":juegos}

      return render(request, "AppPagEntreg/14_leerJuegos.html", contexto)

#____________________________________________________________________________________________________________________________________________________________________________________________
#Funciones que permiten eliminar información

def eliminarPelis(request, peliTitulo):

      pelicula = Peliculas.objects.get(titulo=peliTitulo)
      pelicula.delete()

      pelis = Peliculas.objects.all()

      contexto = {"pelis":pelis}

      return render(request, "AppPagEntreg/12_leerPelis.html", contexto)


def eliminarLibros(request, libroTitulo):

      libro = Libros.objects.get(titulo=libroTitulo)
      libro.delete()

      libros = Libros.objects.all()

      contexto = {"libros":libros}

      return render(request, "AppPagEntreg/13_leerLibros.html", contexto)


def eliminarJuegos(request, juegoNombre):

      juego = Juegos.objects.get(nombre=juegoNombre)
      juego.delete()

      juegos = Juegos.objects.all()

      contexto = {"juegos":juegos}

      return render(request, "AppPagEntreg/14_leerJuegos.html", contexto)

#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#Funciones que permiten modificar información



def modificarPelis(request, peliTitulo):

      pelicula = Peliculas.objects.get(titulo=peliTitulo)

      if request.method == "POST":

            miFormulario = FormularioPeliculas(request.POST)

            if miFormulario.is_valid():

                  informacion = miFormulario.cleaned_data

                  pelicula.titulo = informacion["Título"]
                  pelicula.puntaje = informacion["Puntaje"]

                  pelicula.save()

                  return render(request, "AppPagEntreg/2_Inicio.html")

      else: 

            miFormulario = FormularioPeliculas(initial={"Título":pelicula.titulo, "Puntaje":pelicula.puntaje})

      return render(request, "AppPagEntreg/15_editarPelis.html", {"miFormulario":miFormulario, "titulo":peliTitulo})
      


def modificarLibros(request, libroTitulo):

      libro = Libros.objects.get(titulo=libroTitulo)

      if request.method == "POST":

            miFormulario = FormularioLibros(request.POST)

            if miFormulario.is_valid():

                  informacion = miFormulario.cleaned_data

                  libro.titulo = informacion["Título"]
                  libro.puntaje = informacion["Puntaje"]

                  libro.save()

                  return render(request, "AppPagEntreg/2_Inicio.html")

      else: 

            miFormulario = FormularioLibros(initial={"Título":libro.titulo, "Puntaje":libro.puntaje})

      return render(request, "AppPagEntreg/16_editarLibros.html", {"miFormulario":miFormulario, "titulo":libroTitulo})



def modificarJuegos(request, juegoNombre):

      juego = Juegos.objects.get(nombre=juegoNombre)

      if request.method == "POST":

            miFormulario = FormularioJuegos(request.POST)

            if miFormulario.is_valid():

                  informacion = miFormulario.cleaned_data

                  juego.titulo = informacion["Nombre"]
                  juego.puntaje = informacion["Puntaje"]

                  juego.save()

                  return render(request, "AppPagEntreg/2_Inicio.html")

      else: 

            miFormulario = FormularioJuegos(initial={"Nombre":juego.nombre, "Puntaje":juego.puntaje})

      return render(request, "AppPagEntreg/17_editarJuegos.html", {"miFormulario":miFormulario, "nombre":juegoNombre})