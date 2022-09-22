from django.shortcuts import render
from django.http import HttpResponse
from AppPagEntreg.models import Libros, Peliculas, Juegos

# Create your views here.

def inicio(request):
    return render(request, "AppPagEntreg/2_Inicio.html")


def formularioAdd(request):
    pass


def formularioGet(request):
    pass
