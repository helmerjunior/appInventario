# -*- coding: utf-8 -*-
from appInventario.forms import *
from appInventario.models import Articulo,Cliente, Evento, Servicio
from sisInventario.settings import LOGIN_URL
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from datetime import datetime
from serializers import EventoSerializer, UserSerializer
from rest_framework import viewsets

# Create your views here.
def index_ingresar(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario,password=clave)
            if acceso is not None and acceso.is_active:
                login(request,acceso)
                return HttpResponseRedirect('/menu')
            else:
                return HttpResponseRedirect("/")
    else:
        formulario = AuthenticationForm()
        formulario.fields['username'].widget.attrs["class"] = "form-control input-sm bounceIn animation-delay2"
        formulario.fields['username'].widget.attrs["placeholder"] = "Usuario"
        formulario.fields['password'].widget.attrs["class"] = "form-control input-sm bounceIn animation-delay4"
        formulario.fields['password'].widget.attrs["placeholder"] = "Contraseña"
    return render_to_response('index.html',{'formulario':formulario} ,context_instance=RequestContext(request))

def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required(login_url=LOGIN_URL)
def menu(request):
    num_articulos = Articulo.objects.count()
    num_clientes = Cliente.objects.count()
    num_eventos = Evento.objects.count()
    #este se utilizara para numero de ventas
    mes_actual = datetime.now().month
    usuario = request.user
    lista = {'cantidad_articulos':num_articulos,'usuario':usuario,'cantidad_clientes':num_clientes,'cantidad_eventos':num_eventos}
    return render_to_response('menu.html', lista ,context_instance=RequestContext(request))

@login_required(login_url=LOGIN_URL)
def nuevo_articulo(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = ArticuloForm(request.POST)
        if formulario.is_valid():
            formulario.save(commit=True)
            return HttpResponseRedirect('/articulos/')
        else:
            print formulario.cleaned_data['id_pertenece']
    else:
        formulario = ArticuloForm({'id_pertenece':request.user,'fecha_compra':datetime.now().strftime('%d/%m/%Y')})
    lista = {'formulario':formulario,'usuario':usuario}
    return render_to_response('regArticulo.html',lista, context_instance=RequestContext(request))

@login_required(login_url=LOGIN_URL)
def listar_articulos(request):
    usuario = request.user
    articulos = Articulo.objects.all()
    num_articulos = Articulo.objects.count()
    lista = {'datos':articulos,'cantidad':num_articulos,'usuario':usuario}
    return render_to_response('listArticulo.html',lista, context_instance=RequestContext(request))

@login_required(login_url=LOGIN_URL)
def nuevo_cliente(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save(commit=True)
            return HttpResponseRedirect('/clientes/')
    else:
        formulario = ClienteForm()
    lista = {'formulario_cliente':formulario,'usuario':usuario}
    return render_to_response('regCliente.html',lista,context_instance = RequestContext(request))

@login_required(login_url=LOGIN_URL)
def listar_clientes(request):
    usuario = request.user
    clientes = Cliente.objects.all()
    num_cliente = Cliente.objects.count()
    lista = {'clientes':clientes,'cantidad':num_cliente,'usuario':usuario}
    return render_to_response('listCliente.html', lista ,context_instance=RequestContext(request))

'''
@login_required(login_url=LOGIN_URL)
def nuevo_evento(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = EventoForm(request.POST)
        print formulario.is_valid()
        formulario.cleaned_data['start'] = formulario.cleaned_data['start'] + ":00"
        print formulario.cleaned_data['start']
        formulario.cleaned_data['end'] = formulario.cleaned_data['end'] + ":00"
        print formulario.cleaned_data['end']
        if formulario.is_valid():
            #formulario.save(commit=True)
            return HttpResponseRedirect('/eventos/')
    else:
        formulario = EventoForm()
    lista = {'formulario_evento':formulario,'usuario':usuario}
    return render_to_response('regEvento.html',lista,context_instance = RequestContext(request))
'''

@login_required(login_url=LOGIN_URL)
def listar_eventos(request):
    usuario = request.user
    eventos = Evento.objects.all()
    num_eventos = Evento.objects.count()
    lista = {'cantidad':num_eventos,'usuario':usuario}
    return render_to_response('listEvento.html', lista ,context_instance=RequestContext(request))

@login_required(login_url=LOGIN_URL)
def nuevo_servicio(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = ServicioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/servicios/')
    else:
        formulario = ServicioForm()
    lista = {'formulario_servicio':formulario,'usuario':usuario}
    return render_to_response('regServicio.html',lista,context_instance = RequestContext(request))

@login_required(login_url=LOGIN_URL)
def listar_servicios(request):
    usuario = request.user
    servicios = Servicio.objects.order_by('fecha_servicio')
    num_servicios = Servicio.objects.count()
    lista = {'servicios':servicios,'cantidad':num_servicios,'usuario':usuario}
    return render_to_response('listServicio.html', lista ,context_instance=RequestContext(request))

@login_required(login_url=LOGIN_URL)
def pre_venta(request):
    usuario = request.user
    articulos = Articulo.objects.all
    viene_de_ventas = True
    lista = {'datos':articulos,'usuario':usuario,'viene_de_ventas':viene_de_ventas}
    return render_to_response('listArticulo.html',lista,context_instance=RequestContext(request))

@login_required(login_url=LOGIN_URL)
def venta_por_id(request,articulo_id):
    usuario = request.user
    articulo = Articulo.objects.get(id_articulo=articulo_id)
    if request.method == 'POST':
        formulario = PreVentaForm(request.POST)
        if formulario.is_valid():
            print 'Hi'
    else:
        formulario = PreVentaForm()
        formulario.fields['cantidad'].widget.attrs["class"] = "form-control input-sm"
    lista = {'articulo':articulo,'usuario':usuario,'formulario':formulario}
    return render_to_response('preVenta.html',lista,context_instance=RequestContext(request))
    


@login_required(login_url=LOGIN_URL)
def nueva_venta(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = VentaForm(request.POST)
        print formulario.is_valid()
        if formulario.is_valid():
            print "oie cy"
            if formulario.cleaned_data['impuestoventa'] > 0:
                print "oie cy 2"
                print formulario.cleaned_data['cantidad']
                print formulario.cleaned_data['fk_articulo']
                formulario.cleaned_data['pago_total'] = 666
                print formulario.cleaned_data['pago_total']
                zuqulento = Articulo.objects.filter(nombre=formulario.cleaned_data['fk_articulo'])
                print zuqulento
                #formulario.save(commit=True)
            return HttpResponseRedirect('/ventas/')
        else:
            return HttpResponseRedirect('/ventas/registrar')
    else:
        formulario = VentaForm({'fk_duenioventa':request.user,'fecha':datetime.now().strftime('%d/%m/%Y'),'pago_total':'1.00'})
    lista = {'formulario':formulario,'usuario':usuario}
    return render_to_response('regVenta.html',lista, context_instance=RequestContext(request))



class EventoViewSet(viewsets.ModelViewSet):
    #esto muestra el tiempo adelantado a UTC 1
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer