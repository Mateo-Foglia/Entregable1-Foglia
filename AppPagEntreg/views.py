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

            if miFormulario.is_valid:

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
#Función que permite vizualizar todo el material almacenado

def leerTodo(request):

      pelis = Peliculas.objects.all()
      juegos = Juegos.objects.all()
      libros = Libros.objects.all()

      contexto = {"pelis":pelis, "juegos":juegos, "libros":libros}

      return render(request, "AppPagEntreg/12_leerTodo.html", contexto)

