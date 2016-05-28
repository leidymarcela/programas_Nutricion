# -*- encoding: utf-8 -*-
from .models import Usuario
from django.contrib import auth
from .models import beneficiario

class Validator(object):
    _post = None
    required =[]
    _message = ''

    def __init__(self,post):

        self._post = post

    def is_empty(self,field):
        if field == '' or field is None:
            return True
        return False

    def is_valid(self):

        for field in self.required:
            if self.is_empty(self._post[field]):

                self._message = 'el campo %s no puede ser vacio' % field
                return False

        return True

    def getMessage(self):
        return self._message

class FormRegistroValidator(Validator):

    def is_valid(self):

        if not super(FormRegistroValidator, self).is_valid():
            return False
        #validar que las contraseñas sehan iguales
        if not self._post['password1'] == self._post['password2']:
            self._message = 'Las contraseñas no  coinciden'

            return False

        if Usuario.objects.filter(email = self._post[('email')]).exists():
            self._message = 'El correo electrónico ya se encuentra registrado'
            return False
        #Por ultimo retornamos que en caso de que todo marche bien es correcto el formulario
        return True

class FormLoginValidator(Validator):
    acceso = None

    def is_valid(self):
        if not super(FormLoginValidator, self).is_valid():
            return False

        usuario = self._post['usuario']
        clave = self._post['clave']

        self.acceso = auth.authenticate(username = usuario, password = clave )
        if self.acceso is None:
            self._message = 'Usuario o contraseña inválido'
            return False
        return True

class FormPostValidator(Validator):

    def is_valid(self):
        if not super(FormPostValidator, self).is_valid():
            return False

        if beneficiario.objects.filter(numero_documento = self._post[('numero_documento')]).exists():
            self._message = 'la persona ya se encuentra registrada'
            return False
        #Por ultimo retornamos que en caso de que todo marche bien es correcto el formulario

        if self._post['comunas'] == '0':
            return False

        if self._post['barrios'] == '0':
            self._message = 'Escoja la barrio donde vives'
            return False
        return True

