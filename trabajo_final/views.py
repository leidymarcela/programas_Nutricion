

# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import NON_FIELD_ERRORS
from .validators import FormRegistroValidator,FormLoginValidator,FormPostValidator
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.core import  serializers
from .models import beneficiario,programa,Barrio,Comuna,tipoDocumento,funcionario
from validators import  Validator
#Create your views here.
def buscar(request):
    """view de los resultados de busqueda
    """
    return render_to_response('buscar.html', context_instance = RequestContext(request))

def login(request):
    """view del login
    """
    #Verificamos que los datos lleguen por el methodo POST

    if request.method == 'POST':
        #Cargamos el formulario (ver forms.py con los datos del POST)
        validator = FormLoginValidator(request.POST)
        #formulario = LoginForm(data = request.POST)
        #Verificamos que los datos esten correctos segun su estructura

        if validator.is_valid():
            # Capturamos las variables que llegan por POST
            usuario = request.POST['usuario']
            clave = request.POST['clave']
            auth.login(request, validator.acceso) # Crear una sesion
            return HttpResponseRedirect('/home')
        else:
            return render_to_response('login.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))

    return render_to_response('login.html', context_instance = RequestContext(request))

def index(request):
    """view principal
    """


    return render_to_response('index.html', context_instance = RequestContext(request) )



def search(request):
    """view de los resultados de busqueda
    """
    beneficiarios = None
    filter = None
    if 'filter' in request.GET.keys():
        filter = request.GET['filter']

        qset = ( Q( name__icontains = filter) |
                Q( apellido__icontains = filter) |
                Q( numero_documento__icontains = filter)
                )
        beneficiarios = beneficiario.objects.filter(qset)


        return render_to_response('buscar.html', {'numero_documento': numero_documento, 'filtro': filter  }, context_instance = RequestContext(request))


@login_required(login_url="/login")
def home(request):
    """view de los resultados de busqueda
    """
    return render_to_response('about.html', context_instance = RequestContext(request))

def barrios(request):
    barrio =  Barrio.objects.filter(comuna_id = request.GET['comuna'])
    data = serializers.serialize('json', barrio, fields=('id','name'))
    return HttpResponse( data , content_type ='application/json' )


from django.db import transaction
@transaction.atomic
def post(request):
    programas=programa.objects.all()
    documentos = tipoDocumento.objects.all()

    """view principal
    """
    error = False
    comunas = Comuna.objects.all()
    barrios = Barrio.objects.all()
    if request.method == 'POST':
        validator = FormPostValidator(request.POST)
        validator.required = ['name','apellido','documentos','numero_documento','direccion','barrios','comunas','genero','fecha_de_nacimiento','eps','programass']

        if validator.is_valid():
            beneficiarios = beneficiario()
            #p = Persona.objects.get(documento = '123123123321')
            beneficiarios.name = request.POST['name']
            beneficiarios.apellido= request.POST['apellido']
            beneficiarios.documento_id = request.POST['documentos']
            beneficiarios.numero_documento = request.POST['numero_documento']
            beneficiarios.direccion = request.POST['direccion']
            beneficiarios.barrio_id= request.POST['barrios']
            beneficiarios.genero = request.POST['genero']
            beneficiarios.fecha_de_nacimiento = request.POST['fecha_de_nacimiento']
            beneficiarios.eps = request.POST['eps']
            beneficiarios.programa_id = request.POST['programass']
            beneficiarios.is_active = True
            beneficiarios.save()

            return render_to_response('post.html', {'success': True} , context_instance = RequestContext(request))
        else:
            return render_to_response('post.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))
        # Agregar el usuario a la base de datos
    return render_to_response('post.html',{'programas':programas, 'barrios':barrios,'comunas':comunas,'documentos':documentos}, context_instance = RequestContext(request))



@login_required(login_url="/login") # Protegemos la vista con el decorador del loguin para que solo pueda ingresar un usuario logueado
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")



from django.contrib.auth.hashers import make_password
from .models import Usuario


def contact(request):
    """view del profile
    """

    error = False
    if request.method == 'POST':
        validator = FormRegistroValidator(request.POST)
        validator.required = ['name', 'email','password1','password2']

        if validator.is_valid():
            usuario = User()
            #p = Persona.objects.get(documento = '123123123321')
            usuario.first_name = request.POST['name']
            usuario.username = request.POST['name']
            usuario.email = request.POST['email']
            usuario.password = make_password(request.POST['password1'])
            #TODO: ENviar correo electronico para confirmar cuenta
            usuario.is_active = True

            usuario.save()


            return render_to_response('contact.html', {'success': True  } , context_instance = RequestContext(request))
        else:
            return render_to_response('contact.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))
        # Agregar el usuario a la base de datos
    return render_to_response('contact.html', context_instance = RequestContext(request))

@login_required(login_url='/login')
def regster(request):
    if request.user.groups.filter(id = 2).exists():
        return render_to_response('post.html', context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect('/login')


def listado_programas(request):
    rows = beneficiario.objects.filter( programa_id =  request.GET['programa'])
    return render_to_response('programas.html', {'rows': rows} , context_instance = RequestContext(request))


def programas(request):
     rows = beneficiario.objects.filter( programa_id =  request.GET['programa'])
     return render_to_response('programas.html', {'rows': rows} , context_instance = RequestContext(request))

@login_required(login_url="/login")
def me(request):
    """view del profile
    """
    # si el metodo get no encuentra un objeto genera una excepcion DoesNotExist


    usuario = User.objects.get( id = request.user.id )

    return render_to_response('about.html', { "usuario": usuario, } , context_instance = RequestContext(request))


