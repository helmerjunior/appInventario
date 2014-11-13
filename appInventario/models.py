# encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Modelo del objeto.
class Articulo(models.Model):
    id_articulo = models.AutoField(primary_key=True)
    id_pertenece = models.ForeignKey(User)
    nombre = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    TIPO_CATEGORIA = (
        ('PEL', 'Peluche'),
        ('COL', 'Collar'),
        ('SOR', 'Sortija'),
        ('FIG', 'Figura'),
        ('EST', 'Estatuilla'),
        ('HER', 'Heroclix'),
        ('TCG', 'Juego de Cartas'),
    )
    categoria = models.CharField(max_length=30, choices=TIPO_CATEGORIA)
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.01)])
    precio_venta = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.01)])
    fecha_compra = models.DateField()
    # poner usuario que ingreso el articulo

    def __unicode__(self):
        return self.nombre

    def _retornarid(self):
        return self.id_articulo

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    ap_paterno = models.CharField(max_length=30, blank=True)
    ap_materno = models.CharField(max_length=30, blank=True)
    dni = models.CharField(max_length=8, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    celular = models.CharField(max_length=15, blank=True)

    def __unicode__(self):
        return self.nombre


class VentaArticulo(models.Model):
    id_venta = models.AutoField(primary_key=True)
    # articulo vendido
    fk_articulo = models.ForeignKey(Articulo)
    # el cliente que solicito la venta
    fk_cliente = models.ForeignKey(Cliente)
    # el que hizo la venta
    fk_duenioventa = models.ForeignKey(User,related_name="fk_duenioventa")
    # lo que se le paga a la otra persona
    impuestoventa = models.DecimalField(blank=True,max_digits=5, decimal_places=2, validators=[MinValueValidator(0.01)])
    fk_duenioimpuesto = models.ForeignKey(User,related_name="fk_duenioimpuesto",blank=True)
    cantidad = models.IntegerField()
    # este valor debe ser calculado
    pago_total = models.DecimalField(blank=True,max_digits=5, decimal_places=2, validators=[MinValueValidator(0.01)])
    fecha = models.DateField()



class Servicio(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.01)])
    fecha_servicio = models.DateField(blank=True)

    def __unicode__(self):
        return self.nombre


class Evento(models.Model):
    title = models.CharField(max_length=40)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True)
    allDay = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title