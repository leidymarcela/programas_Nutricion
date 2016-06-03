"""
WSGI config for untitled1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""



import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "programas_nutricion.settings")
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from dj_static import Cling

application = Cling(get_wsgi_application())
application = get_wsgi_application()
application = DjangoWhiteNoise(application)




# Para modo desarrollo
""""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "programas_nutricion.settings")

application = get_wsgi_application()"""
