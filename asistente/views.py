# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from asistente.forms import RegistroForm
from .forms import AgregarAct
from .models import Actividad

class RegistroUsuario(CreateView):
    model=User
    template_name="registro.html"
    form_class=RegistroForm
    success_url=reverse_lazy("index")

# Create your views here.
def pendientes(request):
    Actividad_list=Actividad.objects.order_by('antesde')
    context = {'Actividad_list': Actividad_list}
    return render(request, "pendientes.html", context)

def perfil(request):
    context={}
    return render(request, "perfil.html", context)


def aburrido(request):
    Actividad_list = Actividad.objects.order_by('tiempo')
    context = {'Actividad_list': Actividad_list}
    return render(request, "aburrido.html", context)

def agregar(request): #Mero formulario
    form = AgregarAct(request.POST or None)
    print request.user
    if form.is_valid():
        form_data=form.cleaned_data
        abc1=form_data.get("cosa")
        abc2=form_data.get("tiempo")
        abc3=form_data.get("unidad")
        abc4=form_data.get("antesde")
        if abc3=="Horas":
            abc2=abc2*60
        obj=Actividad.objects.create(usuario=request.user,cosa=abc1,estado="sinempezar",tiempo=abc2,antesde=abc4)
    context={
    "form":form,
    }
    return render(request, "agregar.html", context)

def presentacion(request):
    context={}
    return render(request, "presentacion.html", context)
