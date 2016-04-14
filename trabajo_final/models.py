from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

lst_sexo=(("M","masculino"),("F","femenino"))
class beneficiario(models.Model):
    nombres = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.CharField(max_length=12)
    email = models.EmailField(max_length=30)
    sexo = models.CharField(max_length=1,choices=lst_sexo)

class programa(models.Model):
    nombre = models.CharField(max_length=50)

class funcionario(models.Model):
    nombres = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.CharField(max_length=12)
    email = models.EmailField(max_length=30)
    sexo = models.CharField(max_length=1,choices=lst_sexo)

class entidad(models.Model):
    nombre = models.CharField(max_length=50)

class Usuario(User):
    class Meta:
        proxy = True

