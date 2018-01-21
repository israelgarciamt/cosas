from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class RegistroForm(UserCreationForm):

    class Meta:
        model=User
        fields=[
            "username",
            "first_name",
            "last_name",
            "email",
        ]
        labels={
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Email',
        }

class AgregarAct(forms.Form):
    Minutos = 'Minutos'
    Horas = 'Horas'
    Elegirunidad = (
        (Minutos, u"Minutos"),
        (Horas, u"Horas"),
    )
    cosa=forms.CharField(max_length=500)
    tiempo=forms.IntegerField()
    unidad=forms.ChoiceField(choices=Elegirunidad)
    antesde=forms.DateField()
