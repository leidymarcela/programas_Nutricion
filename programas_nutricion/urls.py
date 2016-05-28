"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from django.conf.urls import url, include
from django.contrib import admin
from trabajo_final.views import *
from django.conf.urls import patterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',login, name='login'),
    url(r'^logon$', logon, name='logon'),
    url(r'^logout$', logout, name='logout'),
    url(r'^menu$', menu, name='menu'),
    url(r'^registro_beneficiario$', registro_beneficiario, name='registro'),
    url(r'^busqueda_beneficiario$', busqueda_beneficiario, name='busqueda'),
    url(r'^buscar_beneficiario/$', buscar_beneficiario),
    url(r'^lista_beneficiario$', lista_beneficiario, name='lista'),
    url(r'^listar_beneficiarios$', listar_beneficiario, name='lista_resultado'),
    url(r'^guardar_beneficiario$', guardar_beneficiario, name='guardar'),
    url(r'^modificar_beneficiario$', modificar_beneficiario, name='modificar_beneficiario'),
    url(r'^generar_pdf$', generate_PDF, name='lista_pdf'),
    url(r'^crear_usuario$', crear_usuario, name='crear usuario'),
    url('^barrio/$', buscar_barrios, name='barrio'),



    url(r'^index$',index, name='index'), # /
    url(r'^contact$', contact, name='contact'),
    url(r'^home$',home, name='home'), #/about


    url('^search$', search, name='search'),

    url(r'^post$',post, name='post'),
    url(r'^listado_programas', listado_programas, name='programa'),
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^buscar$',buscar, name='buscar'),
    url(r'^programas$',programas, name='programas'),
    url('^me$', me, name = 'me' ),
    url('^reportes$', reportes, name = 'reportes' )

    ]
