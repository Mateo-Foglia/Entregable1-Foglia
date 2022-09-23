from django.shortcuts import render
from django.http import HttpResponse
from AppPagEntreg.models import Libros, Peliculas, Juegos

# Create your views here.

def inicio(request):
    return render(request, "AppPagEntreg/2_Inicio.html")


def addLibro(request):
    return render(request, "AppPagEntreg/3_addLibro.html")


def addJuego(request):
    pass


def addPeli(request):
    pass


def getLibro(request):
    pass


def getJuego(request):
    pass


def getPeli(request):
    pass
