# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 18:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cosa', models.CharField(max_length=500)),
                ('estado', models.CharField(blank=True, max_length=10)),
                ('tiempo', models.IntegerField()),
                ('antesde', models.DateField(blank=True, null=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('etiquetaarriba', models.CharField(blank=True, max_length=10)),
                ('etiquetaabajo', models.CharField(blank=True, max_length=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
