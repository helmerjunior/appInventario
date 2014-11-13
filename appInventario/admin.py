from django.contrib import admin
from appInventario.models import *

# Register your models here.
admin.site.register(Articulo)
admin.site.register(Cliente)
admin.site.register(VentaArticulo)
admin.site.register(Servicio)
admin.site.register(Evento)