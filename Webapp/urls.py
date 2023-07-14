from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("cliente", views.cliente_view, name="cliente"),
    path("empleado", views.empleado_view, name="empleado"),
    path("registro", views.registro, name="registro"),
    path("exito", views.exito, name="exito"),
    path("error", views.error, name="error"),
    path("inicioSesion", views.inicioSesion, name="inicioSesion"),
    path("actualizarCliente", views.actualizarCliente, name="actualizarCliente"),
    path("enviarSolicitud", views.enviarSolicitud, name="enviarSolicitud"),
    path("salir", views.salir, name="salir"),
    path("aceptarSolicitud", views.aceptarSolicitud, name="aceptarSolicitud"),
    path("crearContratoCaso", views.crearContratoCaso, name="crearContratoCaso"),
    path("detalles/<int:pk>", views.detalles, name="detalles"),
    path("enviarDiligencia", views.enviarDiligencia, name="enviarDiligencia"),
    path("enviarDocumento", views.enviarDocumento, name="enviarDocumento"),
]

