# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Actividad(models.Model):
    usuario=models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    cosa=models.CharField(max_length=500)
    estado=models.CharField(max_length=10, blank=True, null=False)
    tiempo=models.IntegerField()
    antesde=models.DateField(null=True, blank=True)
    timestamp=models.DateField(auto_now_add=True, auto_now=False)
    etiquetaarriba=models.CharField(max_length=10, blank=True, null=False)
    etiquetaabajo=models.CharField(max_length=10, blank=True, null=False)
    def __unicode__(self):
        return self.cosa
