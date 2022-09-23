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
    
    if request.GET["Puntaje"]:
        
        puntaje = request.GET["Puntaje"]
        libros = Libros.objects.filter(puntaje__iexact=puntaje)
        
        return render(request, "AppPagEntreg/9_resultadosLibros.html", {"libros":libros, "puntaje":puntaje})
    
    else:

        respuesta = "Tenés que ingresar datos."

        return HttpResponse(respuesta)




def getJuego(request):

    return render(request, "AppPagEntreg/8_getJuego.html")


def buscarJuego(request):

      if request.GET["Puntaje"]:

            puntaje = request.GET["Puntaje"]
            juegos = Juegos.objects.filter(puntaje__iexact=puntaje)

            return render(request, "AppPagEntreg/10_resultadosJuegos.html", {"juegos":juegos, "puntaje":puntaje})

      else:

            respuesta = "Tenés que ingresar datos."

            return HttpResponse(respuesta)





def getPeli(request):

    return render(request, "AppPagEntreg/7_getPeli.html")


def buscarPeli(request):

      if request.GET["Puntaje"]:

            puntaje = request.GET["Puntaje"]
            pelis = Peliculas.objects.filter(puntaje__iexact=puntaje)

            return render(request, "AppPagEntreg/11_resultadosPelículas.html", {"pelis":pelis, "puntaje":puntaje})

      else:

            respuesta = "Tenés que ingresar datos."

            return HttpResponse(respuesta)