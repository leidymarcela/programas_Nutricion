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
    url(r'^index$',index, name='index'), # /
    url(r'^contact$', contact, name='contact'),
    url(r'^home$',home, name='home'), #/about
    url(r'^$',login, name='login'),
    url('^search$', search, name='search'),
    url('^barrio$', barrios, name='barrio'),
    url(r'^post$',post, name='post'),
    url(r'^listado_programas', listado_programas, name='programa'),
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^buscar$',buscar, name='buscar'),
    url(r'^programas$',programas, name='programas'),
    url('^me$', me, name = 'me' ),
]
