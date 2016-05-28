# -*- encoding: utf-8 -*-
import datetime

from django.db import transaction
from django.core import serializers
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import NON_FIELD_ERRORS
from .validators import FormRegistroValidator,FormLoginValidator,FormPostValidator
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.http import Http404
from .models import *
from validators import Validator
#import xhtml2pdf.pisa as pisa
##from StringIO  import StringIO
from django.template.loader import render_to_string, get_template
from programas_nutricion.settings import STATICFILES_DIRS
import json
import weasyprint

#Create your views here.

#login , logon y logout

def login(request):
     return render_to_response('login/login.html', context_instance = RequestContext(request))

def logon(request):

    if request.method == 'POST':
        validator = FormLoginValidator(request.POST)

        if validator.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            auth.login(request, validator.acceso)

            return HttpResponseRedirect('/menu')
        else:
            return render_to_response('login/login.html', {'error': validator.getMessage() } , context_instance = RequestContext(request))

    return render_to_response('login/login.html', context_instance = RequestContext(request))

@login_required(login_url="/")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

# fin de login y logon

# manejo de dashboard
def menu(request):
    return render_to_response('dashboard/menu.html', context_instance = RequestContext(request))
# fin de dashboard

# manejo de beneficiarios
@login_required(login_url="/")
def registro_beneficiario(request):

    if request.session.has_key('aviso'):
        indicador = 1
        aviso = request.session.get('aviso')
        del request.session['aviso']

    elif request.session.has_key('error'):
        indicador = 0
        aviso = request.session.get('error')
        del request.session['error']
    else:
        indicador = ''
        aviso = "Por favor llene todos los campos de la pantalla"

    programa = Programa.objects.all()
    documento = TipoDocumento.objects.all()
    comuna = Comuna.objects.all()
    barrio = Barrio.objects.all()
    eps = Eps.objects.all()

    return render_to_response('beneficiarios/registro_beneficiario.html', {'programa':programa, 'documento':documento, 'comuna':comuna, 'barrio':barrio, 'indicador':indicador,'respuesta':aviso, 'eps':eps},context_instance = RequestContext(request))

@login_required(login_url="/")
def lista_beneficiario(request):
    programa = Programa.objects.all()
    return render_to_response('beneficiarios/lista_beneficiario.html',{'programa':programa}, context_instance = RequestContext(request))

@login_required(login_url="/")
def busqueda_beneficiario(request):

    if request.session.has_key('aviso'):
        indicador = 1
        aviso = request.session.get('aviso')
        del request.session['aviso']

    elif request.session.has_key('error'):
        indicador = 0
        aviso = request.session.get('error')
        del request.session['error']
    else:
        indicador = ''
        aviso = "Favor busque el beneficiario para continuar"

    programa = Programa.objects.all()
    documento = TipoDocumento.objects.all()
    comuna = Comuna.objects.all()
    barrio = Barrio.objects.all()
    eps = Eps.objects.all()

    return render_to_response('beneficiarios/busqueda_beneficiario.html', {'indicador':indicador,'respuesta':aviso, 'programa':programa, 'documento':documento, 'comuna':comuna, 'barrio':barrio, 'eps':eps}, context_instance = RequestContext(request))

@login_required(login_url="/")
def listar_beneficiario(request):
    try:
        programa = Programa.objects.all()

        if request.POST['programa'] == '':
            busqueda = Beneficiario.objects.filter(fecha_registro__range =(request.POST['fechainicial'], request.POST['fechafinal']))
        else:
            busqueda = Beneficiario.objects.filter(fecha_registro__range =(request.POST['fechainicial'], request.POST['fechafinal']), programa= request.POST['programa'])
        cont = len(busqueda)
        indicador=1
        if cont == 1:
            respuesta = 'Consulta realizada con exito, se han encontrado '+ str(cont) +' beneficiario'
        elif cont == 0:
            indicador = 2
            respuesta = 'Consulta realizada con exito, no se encontraron beneficiarios'
        else:
            respuesta = 'Consulta realizada con exito, se han encontrado '+ str(cont) +' beneficiarios'

        datos = {'fechainicial':request.POST['fechainicial'], 'fechafinal': request.POST['fechafinal'], 'programa':request.POST['programa']}
        request.session['lista_programas'] = datos

        return  render_to_response('beneficiarios/lista_beneficiario.html', {'programa':programa,"resultado": busqueda, 'indicador':indicador, 'respuesta':respuesta}, context_instance = RequestContext(request))

    except:

        indicador = 0
        respuesta = 'no se pudo realizar la consulta, comuniquese con el administrador del sistema'
        busqueda = ''

        return  render_to_response('beneficiarios/lista_beneficiario.html', {"resultado": busqueda, 'indicador':indicador, 'respuesta':respuesta}, context_instance = RequestContext(request))

@login_required(login_url="/")
def guardar_beneficiario(request):

    if request.method == 'POST':
        beneficiario = Beneficiario()
        beneficiario.name = request.POST['nombre']
        beneficiario.apellido = request.POST['apellido']
        beneficiario.documento_id = request.POST['documento']
        beneficiario.numero_documento = request.POST['numero_documento']
        beneficiario.fecha_de_nacimiento = request.POST['fecha_nacimiento']
        beneficiario.direccion = request.POST['direccion']
        beneficiario.barrio_id = request.POST['barrio']
        beneficiario.fecha_registro = datetime.date.today()
        beneficiario.hora_registro = datetime.datetime.now()
        beneficiario.genero = request.POST['genero']
        beneficiario.eps_id = request.POST['eps']
        beneficiario.programa_id = request.POST['programa']

        beneficiario.save()

        request.session['aviso'] = 'El Beneficiario se ha guardado con exito'
        return HttpResponseRedirect('/registro_beneficiario')
    else:
        request.session['error'] = 'El guardado no se pudo completar, comuniquese con el administrador del sistema'
        return HttpResponseRedirect('/registro_beneficiario')

def buscar_beneficiario(request):
    documento = request.GET['numero_documento']
    try:
        beneficiario = Beneficiario.objects.get( numero_documento= documento)
        resultado = 1

        output = { 'resultado': resultado,'name': beneficiario.name, "apellido": beneficiario.apellido, 'documento':beneficiario.documento.name, 'documento_id':beneficiario.documento.id, 'numero_documento':beneficiario.numero_documento,'id':beneficiario.id,'programa':beneficiario.programa.name,'programa_id':beneficiario.programa.id,'direccion':beneficiario.direccion,'barrio':beneficiario.barrio.name,'comuna':beneficiario.barrio.comuna_id, 'barrio_id':beneficiario.barrio.id,'fecha_de_nacimiento':str(beneficiario.fecha_de_nacimiento), 'fecha_registro':str(beneficiario.fecha_registro),'eps':beneficiario.eps.name,'eps_id':beneficiario.eps.id}

        return HttpResponse(json.dumps(output),  content_type="application/json")
    except Beneficiario.DoesNotExist:
        output = {'error': 0, 'resultado': 0}
        return HttpResponse(json.dumps(output),  content_type="application/json")

def buscar_barrios(request):
    barrio =  Barrio.objects.filter(comuna_id = request.GET['comuna'])
    data = serializers.serialize('json', barrio, fields=('id','name'))
    return HttpResponse( data , content_type ='application/json' )

@login_required(login_url="/")
def modificar_beneficiario(request):

    if request.method == 'POST':
        beneficiario = Beneficiario.objects.get(id= request.POST['ids'] )

        if request.POST['nombre'] != beneficiario.name:
            beneficiario.name = request.POST['nombre']

        if request.POST['apellido'] != beneficiario.apellido:
            beneficiario.apellido = request.POST['apellido']

        if not str(request.POST['documento']) == str(beneficiario.documento_id):
            beneficiario.documento_id = request.POST['documento']

        if request.POST['numero_documento'] != beneficiario.numero_documento:
            beneficiario.numero_documento = request.POST['numero_documento']

        if not str(request.POST['fecha_nacimiento']) == str(beneficiario.fecha_de_nacimiento):
            beneficiario.fecha_de_nacimiento = request.POST['fecha_nacimiento']

        if request.POST['direccion'] != beneficiario.direccion:
            beneficiario.direccion = request.POST['direccion']

        if not str(request.POST['barrio']) == str(beneficiario.barrio_id):
            beneficiario.barrio_id = request.POST['barrio']

        if not str(request.POST['eps']) == str(beneficiario.eps.id):
            beneficiario.eps_id = request.POST['eps']

        if not str(request.POST['programa']) == str(beneficiario.programa.id):
            beneficiario.programa_id = request.POST['programa']

        beneficiario.save()

        request.session['aviso'] = 'El Beneficiario se ha modificado correctamente'
        return HttpResponseRedirect('/busqueda_beneficiario')
    else:
        request.session['error'] = 'El guardado no se pudo completar, comuniquese con el administrador del sistema'
        return HttpResponseRedirect('/busqueda_beneficiario')

# fin de manejo de beneficiarios

# pdf

@login_required(login_url='/')
def generate_PDF(request):
    if request.session.has_key('lista_programas'):
        dato = request.session.get('lista_programas')
        del request.session['lista_programas']

        if dato['programa'] == '':
            busqueda = Beneficiario.objects.filter(fecha_registro__range =(dato['fechainicial'], dato['fechafinal']))
        else:
            busqueda = Beneficiario.objects.filter(fecha_registro__range =(dato['fechainicial'], dato['fechafinal']), programa= dato['programa'])


        template = get_template("listado_beneficiarios.html")
        context = {"beneficiarios": busqueda}
        html = template.render(RequestContext(request, context))
        response = HttpResponse(content_type='application/pdf')
        weasyprint.HTML(string=html,base_url=request.build_absolute_uri()).write_pdf(response)

        return response
    else:
        return HttpResponse("La etiqueta no ha podido ser generada")

# fin de pdf

# gestion de usuarios

@login_required(login_url="/")
def crear_usuario(request):

    return render_to_response('usuarios/crear_usuario.html',{}, context_instance = RequestContext(request))


# fin de usuarios



def pdf(f):
    def funcion(*args, **kwargs):
        html = f(*args, **kwargs)
        result = StringIO() #creamos una instancia del un objeto StringIO para
        pdf = pisa.pisaDocument( html , result) # convertimos en pdf la template
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return funcion

@pdf
def reportes(request):
    beneficiarios = Beneficiario.objects.get(id = request.GET['beneficiarios'])
    return render_to_string("reportes.html", { 'beneficiario': Beneficiario, 'path': STATICFILES_DIRS[0]}) #obtenemos la plantilla


def buscar(request):
    """view de los resultados de busqueda
    """
    return render_to_response('buscar.html', context_instance = RequestContext(request))


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
        filter = request.GET['documento']

        qset = (Q( numero_documento__icontains = filter) )
        beneficiarios = Beneficiario.objects.filter(qset)


    return render_to_response('buscar.html', {'beneficiarios': beneficiarios, 'filtro': filter  }, context_instance = RequestContext(request))

@login_required(login_url="/login")
def home(request):
    """view de los resultados de busqueda
    """
    return render_to_response('about.html', context_instance = RequestContext(request))




@transaction.atomic
def post(request):
    programas=Programa.objects.all()
    documentos = TipoDocumento.objects.all()

    """view principal
    """
    error = False
    comunas = Comuna.objects.all()
    barrios = Barrio.objects.all()
    if request.method == 'POST':
        validator = FormPostValidator(request.POST)
        validator.required = ['name','apellido','documentos','numero_documento','direccion','barrios','comunas','genero','fecha_de_nacimiento','eps','programass']

        if validator.is_valid():
            beneficiarios = Beneficiario()
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
    rows = Beneficiario.objects.filter(programa_id =  request.GET['programa'])
    return render_to_response('programas.html', {'rows': rows} , context_instance = RequestContext(request))


def programas(request):
     rows = Beneficiario.objects.filter(programa_id =  request.GET['programa'])
     return render_to_response('programas.html', {'rows': rows} , context_instance = RequestContext(request))

@login_required(login_url="/login")
def me(request):
    """view del profile
    """
    # si el metodo get no encuentra un objeto genera una excepcion DoesNotExist


    usuario = User.objects.get( id = request.user.id )

    return render_to_response('about.html', { "usuario": usuario, } , context_instance = RequestContext(request))


