from django.forms import ModelForm, TextInput, Select, NumberInput, DateInput,DateTimeInput
from django import forms
from appInventario.models import Articulo, Cliente, Evento, Servicio, User, VentaArticulo



class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        widgets = {
            'id_pertenece' : Select(choices=User.objects.all(),attrs={'class':'form-control','data-required':'true'}),
            'nombre': TextInput(attrs={'class':'form-control input-sm','data-required':'true'}),
            'stock': NumberInput(attrs={'class':'form-control input-sm','data-required':'true'}),
            'categoria': Select(choices=Articulo.TIPO_CATEGORIA , attrs={'class':'form-control','data-required':'true'}),
            'precio_compra': NumberInput(attrs={'class':'form-control input-sm','data-required':'true','data-min':'0','min':'0'}),
            'precio_venta': NumberInput(attrs={'class':'form-control input-sm','data-required':'true','data-min':'0','min':'0'}),
            'fecha_compra': DateInput(format={'%d/%m/%Y'},attrs={'placeholder':'DD/MM/AAAA','class':'datepicker form-control','data-required':'true'}),
        }

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        widgets = {
            'nombre': TextInput(attrs={'class':'form-control input-sm','data-required':'true','placeholder':'O Sobrenombre xD'}),
            'ap_paterno': TextInput(attrs={'class':'form-control input-sm','placeholder':'No es obligatorio'}),
            'ap_materno': TextInput(attrs={'class':'form-control input-sm','placeholder':'No es obligatorio'}),
            'dni': TextInput(attrs={'class':'form-control input-sm','placeholder':'No es obligatorio'}),
            'telefono': TextInput(attrs={'class':'form-control input-sm','placeholder':'No es obligatorio'}),
            'celular': TextInput(attrs={'class':'form-control input-sm','placeholder':'No es obligatorio'}),
        }

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        widgets ={
            'title': TextInput(attrs={'class':'form-control input-sm','data-required':'true'}),
            'start': DateTimeInput(attrs={'type':'datetime-local'}),
            'end': DateTimeInput(attrs={'type':'datetime-local'}),
        }

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        widgets ={
            'nombre': TextInput(attrs={'class':'form-control input-sm','data-required':'true'}),
            'precio': NumberInput(attrs={'class':'form-control input-sm','data-required':'true'}),
            'fecha_servicio': DateInput(format={'%d/%m/%Y'},attrs={'placeholder':'DD/MM/AAAA','class':'datepicker form-control','data-required':'true'}),
        }

class VentaForm(ModelForm):
    class Meta:
        model = VentaArticulo
        widgets = {
            'fk_articulo' : Select(choices=Articulo.objects.all(),attrs={'class':'form-control','data-required':'true'}),
            'fk_cliente': Select(choices=Cliente.objects.all(),attrs={'class':'form-control','data-required':'true','data-min':'0'}),
            'fk_duenioventa': Select(choices=User.objects.all(),attrs={'class':'form-control','data-required':'true','data-min':'0'}),
            'impuestoventa': NumberInput(attrs={'class':'form-control input-sm','data-required':'true','data-min':'0'}),
            'fk_duenioimpuesto': Select(choices=User.objects.all(),attrs={'class':'form-control','data-required':'true','data-min':'0'}),
            'cantidad': NumberInput(attrs={'class':'form-control input-sm','data-required':'true','data-min':'1','min':'1'}),
            'pago_total': NumberInput(attrs={'class':'form-control input-sm','data-required':'true','data-min':'0'}),
            'fecha': DateInput(format={'%d/%m/%Y'},attrs={'placeholder':'DD/MM/AAAA','class':'datepicker form-control','data-required':'true'}),
        }

class PreVentaForm(forms.Form):
    cantidad = forms.IntegerField()