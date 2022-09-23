from django.shortcuts import render
from django.http import HttpResponse
from AppPagEntreg.models import Libros, Peliculas, Juegos

# Create your views here.

def inicio(request):
    return render(request, "AppPagEntreg/2_Inicio.html")


def addLibro(request):

    if request.method == "POST":

        libro = Libros(titulo=request.POST["Título"], autor=request.POST["Autor"], genero=request.POST["Género"])
        libro.save()
        return render(request, "AppPagEntreg/2_Inicio.html")

    return render(request, "AppPagEntreg/3_addLibro.html")


def addJuego(request):
    
    if request.method == "POST":

        juego = Juegos(nombre=request.POST["Nombre"], genero=request.POST["Género"])
        juego.save()
        return render(request, "AppPagEntreg/2_Inicio.html")

    return render(request, "AppPagEntreg/5_addJuego.html")


def addPeli(request):

    if request.method == "POST":

        peli = Peliculas(titulo=request.POST["Título"], duracion=request.POST["Duración"], genero=request.POST["Género"])
        peli.save()
        return render(request, "AppPagEntreg/2_Inicio.html")

    return render(request, "AppPagEntreg/4_addPeli.html")


def getLibro(request):
    return render(request, "AppPagEntreg/6_getLibro.html")


def getJuego(request):
    return render(request, "AppPagEntreg/8_getJuego.html")


def getPeli(request):
    return render(request, "AppPagEntreg/7_getPeli.html")
