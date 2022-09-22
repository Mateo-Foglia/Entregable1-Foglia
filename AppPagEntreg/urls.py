from django.urls import path
from AppPagEntreg.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('formularioAdd/', formularioAdd, name="Añadir categorías"),
    path('formularioGet', formularioGet, name="Buscar categorías"),
]
