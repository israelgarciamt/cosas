# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.apps import AppConfig
# Register your models here.
from asistente.models import Actividad

admin.site.register(Actividad)
