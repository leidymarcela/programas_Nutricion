
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

lst_sexo=(("M","masculino"),("F","femenino"))

class Comuna(models.Model):
    name = models.CharField(max_length=70)

class Barrio(models.Model):
    comuna = models.ForeignKey(Comuna)
    name = models.CharField(max_length=70)

class programa(models.Model):
    name = models.CharField(max_length=120)
    def __unicode__(self):
        return self.name

class tipoDocumento(models.Model):
    name = models.CharField(max_length=120)
    def __unicode__(self):
        return self.name

class beneficiario(models.Model):
    name = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.ForeignKey(tipoDocumento)
    numero_documento = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    barrio= models.ForeignKey(Barrio)
    genero = models.CharField(max_length=1,choices=lst_sexo)
    fecha_de_nacimiento = models.DateField()
    eps = models.CharField(max_length=50)
    programa= models.ForeignKey(programa)

    class Meta:
        verbose_name = 'beneficiario'
        verbose_name_plural = "beneficiarios"

    def __unicode__(self):
        return self.name


class funcionario(models.Model):
    name = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.CharField(max_length=12)
    email = models.EmailField(max_length=30)
    sexo = models.CharField(max_length=1,choices=lst_sexo)
    def __unicode__(self):
        return self.name

class entidad(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Usuario(User):
    class Meta:
        proxy = True


