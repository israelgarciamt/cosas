"""cosas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from asistente import views
from asistente.views import RegistroUsuario
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required #para plantillas que requieran un usuario identificado

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login,{'template_name':'index.html'}, name='login'),
    url(r'^registrarse/', RegistroUsuario.as_view(), name='registrarse'),
    url(r'^pendientes/', login_required(views.pendientes), name='pendientes'),
    url(r'^perfil/', login_required(views.perfil), name='perfil'),
    url(r'^aburrido/', login_required(views.aburrido), name='aburrido'),
    url(r'^agregar/', login_required(views.agregar), name='agregar'),
    url(r'^presentacion/', views.presentacion, name='presentacion'),
]
