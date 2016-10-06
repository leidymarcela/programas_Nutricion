
from __future__ import unicode_literals
from django.db import models
#from tinymce.models import HTMLField
from django.contrib.auth.models import User

lst_sexo=(("M","masculino"),("F","femenino"))

class Comuna(models.Model):
    name = models.CharField(max_length=70)

    class Meta:
        db_table = 'Comuna'

class Barrio(models.Model):
    name = models.CharField(max_length=70)
    comuna = models.ForeignKey('Comuna',models.DO_NOTHING)

    class Meta:
        db_table = 'Barrio'

class Programa(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        db_table = 'Programa'

    def __unicode__(self):
        return self.name

class TipoDocumento(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'TipoDocumento'


    def __unicode__(self):
        return self.name

class Beneficiario(models.Model):
    name = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.ForeignKey('TipoDocumento', models.DO_NOTHING)
    numero_documento = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    barrio= models.ForeignKey('Barrio', models.DO_NOTHING)
    genero = models.CharField(max_length=1,choices=lst_sexo)
    fecha_registro = models.DateField()
    hora_registro = models.TimeField()
    fecha_de_nacimiento = models.DateField()
    eps = models.ForeignKey('Eps', models.DO_NOTHING)
    programa= models.ForeignKey('Programa',models.DO_NOTHING)

    class Meta:
        db_table = 'Beneficiario'
        verbose_name = 'beneficiario'
        verbose_name_plural = "beneficiarios"

    def __unicode__(self):
        return self.name


class Funcionario(models.Model):
    name = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.CharField(max_length=12)
    email = models.EmailField(max_length=30)
    sexo = models.CharField(max_length=1,choices=lst_sexo)

    class Meta:
        db_table = 'Funcionario'

    def __unicode__(self):
        return self.name

class Entidad(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'Entidad'

    def __unicode__(self):
        return self.name

class Eps(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Eps'

    def __unicode__(self):
        return self.name

class Usuario(User):
    class Meta:
        proxy = True


