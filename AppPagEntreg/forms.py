from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioJuegos(forms.Form):
    Nombre = forms.CharField(max_length=60)
    Puntaje = forms.FloatField()

class FormularioLibros(forms.Form):
    Título = forms.CharField(max_length=60)
    Puntaje = forms.FloatField()

class FormularioPeliculas(forms.Form):
    Título = forms.CharField(max_length=60)
    Puntaje = forms.FloatField()

class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repita la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class FormularioEditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repita la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]