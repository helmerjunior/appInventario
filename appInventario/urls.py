from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from .views import EventoViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'links',EventoViewSet)
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
    #api urls
    url(r'^api/',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$','appInventario.views.index_ingresar'),
    url(r'^cerrar/$','appInventario.views.cerrar_sesion'),
    url(r'^menu/$','appInventario.views.menu'),
    url(r'^articulos/registrar$','appInventario.views.nuevo_articulo'),
    url(r'^articulos/$','appInventario.views.listar_articulos'),
    url(r'^eventos/$','appInventario.views.listar_eventos'),
    #url(r'^eventos/registrar$','appInventario.views.nuevo_evento'),
    url(r'^clientes/registrar$','appInventario.views.nuevo_cliente', name='nuevo_cliente'),
    url(r'^clientes/$','appInventario.views.listar_clientes'),
    url(r'^servicios/registrar$','appInventario.views.nuevo_servicio', name='nuevo_servicio'),
    url(r'^servicios/$','appInventario.views.listar_servicios'),
    url(r'^ventas/registrar$','appInventario.views.pre_venta', name='pre_venta'),
    url(r'^ventas/registrar/(?P<articulo_id>\d+)/$','appInventario.views.venta_por_id', name='venta_por_id'),
    #url(r'^ventas/registrar$','appInventario.views.nueva_venta', name='nuevo_servicio'),
    #url(r'^ventas/$','appInventario.views.listar_servicios'),
)
