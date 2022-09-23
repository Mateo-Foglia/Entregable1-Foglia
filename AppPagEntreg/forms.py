from django import forms

class FormularioJuegos(forms.Form):
    Nombre = forms.CharField(max_length=60)
    Puntaje = forms.FloatField()

class FormularioLibros(forms.Form):
    Título = forms.CharField(max_length=60)
    Puntaje = forms.FloatField()

class FormularioPeliculas(forms.Form):
    Título = forms.CharField(max_length=60)
    Puntaje = forms.FloatField()