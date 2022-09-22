from django.urls import path
from AppPagEntreg.views import *

urlpatterns = [
    path('', inicio),
    path('formularioAdd/', formularioAdd),
    path('formularioGet', formularioGet),
]
