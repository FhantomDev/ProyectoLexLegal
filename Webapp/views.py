from django.shortcuts import render, redirect
from .models import comuna, cliente, empleado, solicitud, solicitud_aceptada, contrato, caso, diligencia, documento, boleta
from django.db import IntegrityError
from datetime import datetime
from django.db.models import Sum

# Create your views here.


def index(request):
    context = {

    }
    return render(request, "pages/index.html", context)


def exito(request):
    context = {

    }
    return render(request, "pages/exito.html", context)


def error(request):
    context = {

    }
    return render(request, "pages/error.html", context)


def cliente_view(request):
    run = request.session["runCliente"]
    cli = cliente.objects.get(runCliente=run)
    com = comuna.objects.all()
    sol_aceptada = solicitud_aceptada.objects.all()
    ca = caso.objects.all()

    context = {
        "cliente": cli,
        "comuna": com,
        "aceptada": sol_aceptada,
        "caso": ca,
    }
    return render(request, "pages/cliente.html", context)


def empleado_view(request):
    run = request.session["runEmpleado"]
    emp = empleado.objects.get(runEmpleado=run)
    sol = solicitud.objects.all()
    sol_aceptada = solicitud_aceptada.objects.all()
    ca = caso.objects.all()
    suma_boletas = boleta.objects.aggregate(total=Sum('montoPagoBoleta'))
    context = {
        "empleado": emp,
        "solicitud": sol,
        "aceptada": sol_aceptada,
        "caso": ca,
        "boleta": suma_boletas,
    }
    return render(request, "pages/empleado.html", context)


def detalles(request, pk):
    ca= caso.objects.get(idCaso=pk)
    di = diligencia.objects.filter(caso=pk)
    do = documento.objects.filter(caso=pk)

    context = {
        "caso": ca,
        "diligencia": di,
        "documento": do,
    }
    return render(request, "pages/detalles.html", context)


def enviarDiligencia(request):
    if request.method == "POST":
        idCas = request.POST["idCa"]
        desc = request.POST["diligencia"]
        fecha = datetime.now()
        cas = caso.objects.get(idCaso=idCas)

        objDiligencia = diligencia.objects.create(
            descripcionDiligencia = desc,
            fechaDiligencia = fecha,
            caso = cas,
        )
        objDiligencia.save()

        context = {
            "mensaje": "Diligencia guardada con exito",
            "caso": cas,
        }
        return render(request, "pages/exito.html", context)
    

def enviarDocumento(request):
    if request.method == "POST":
        doc = request.FILES["documento"]
        desc = request.POST["descripcion"]
        idCa = request.POST["idCa"]

        ca = caso.objects.get(idCaso=idCa)

        objDocu = documento.objects.create(
            descripcionDocumento = desc,
            archivoDocumento = doc,
            fechaDocumento = datetime.now(),
            caso = ca,
        )
        objDocu.save()

        context = {
            "mensaje": "Documento guardado con exito"
        }
        return render(request, "pages/exito.html", context)


def registro(request):
    if request.method != "POST":
        com = comuna.objects.all()

        context = {
            "comuna": com,
        }
        return render(request, "pages/registro.html", context)

    else:
        run = request.POST["run"]
        correo = request.POST["email"]
        contraseña = request.POST["password"]
        nombre = request.POST["nombre"]
        apPaterno = request.POST["apPaterno"]
        apMaterno = request.POST["apMaterno"]
        direccion = request.POST["direccion"]
        telefono = request.POST["telefono"]
        comunaCli = request.POST["comuna"]

        objComuna = comuna.objects.get(idComuna=comunaCli)

        try:
            cli = cliente.objects.create(
                runCliente=run,
                correoCliente=correo,
                contraseñaCliente=contraseña,
                nombreCliente=nombre,
                apPaternoCliente=apPaterno,
                apMaternoCliente=apMaterno,
                direccionCliente=direccion,
                telefonoCliente=telefono,
                comuna=objComuna,
            )
            cli.save()

            context = {
                "mensaje": "Registro exitoso"
            }
            return render(request, "pages/exito.html", context)

        except IntegrityError:
            context = {
                "mensaje": "El rut ya está registrado"
            }
            return render(request, "pages/error.html", context)


def inicioSesion(request):
    if request.method == "POST":
        username = request.POST["run"]
        password = request.POST["password"]

        if username and password:
            try:
                cli = cliente.objects.get(
                    runCliente=username, contraseñaCliente=password)
            except cliente.DoesNotExist:
                cli = None
            try:
                emp = empleado.objects.get(
                    runEmpleado=username, contraseñaEmpleado=password)
            except empleado.DoesNotExist:
                emp = None

            if cli is not None:
                request.session["runCliente"] = username
                context = {
                    "mensaje": "Inicio de sesión exitoso"
                }
                return render(request, "pages/exito.html", context)
            elif emp is not None:
                request.session["runEmpleado"] = username
                context = {
                    "mensaje": "Inicio de sesión exitoso",
                }
                return render(request, "pages/exito.html", context)

        context = {"mensaje": "Usuario y/o Contraseña incorrecta"}
        return render(request, "pages/error.html", context)


def actualizarCliente(request):
    if request.method == "POST":
        runCli = request.session["runCliente"]
        cli = cliente.objects.get(runCliente=runCli)

        run = request.POST["run"]
        correo = request.POST["email"]
        contraseña = request.POST["password"]
        nombre = request.POST["nombre"]
        apPaterno = request.POST["apPaterno"]
        apMaterno = request.POST["apMaterno"]
        direccion = request.POST["direccion"]
        telefono = request.POST["telefono"]
        comunaCli = request.POST["comuna"]

        objComuna = comuna.objects.get(idComuna=comunaCli)

        cli.runCliente = run
        cli.correoCliente = correo
        cli.contraseñaCliente = contraseña
        cli.nombreCliente = nombre
        cli.apMaternoCliente = apPaterno
        cli.apMaternoCliente = apMaterno
        cli.direccionCliente = direccion
        cli.telefonoCliente = telefono
        cli.comuna = objComuna
        cli.save()

        context = {
            "mensaje": "Datos Actualizados con exito"
        }

        return render(request, "pages/exito.html", context)


def enviarSolicitud(request):
    if request.method == "POST":
        runCli = request.session["runCliente"]
        cli = cliente.objects.get(runCliente=runCli)

        desc = request.POST["desc-solicitud"]
        fecha = datetime.now()

        sol = solicitud.objects.create(
            descripcionSolicitud = desc,
            fechaSolicitud = fecha,
            cliente = cli,
        )
        sol.save()

        context = {
            "mensaje": "Solicitud enviada con exito",
        }
        return render(request, "pages/exito.html", context)
    

def aceptarSolicitud(request):
    if request.method == "POST":
        runCli = request.POST["cliente"]
        idSol = request.POST["idSolicitud"]
        desc = request.POST["descripcion"]
        fecha = datetime.now()
        pre = request.POST["presupuesto"]

        cli = cliente.objects.get(runCliente=runCli)
        sol = solicitud.objects.get(idSolicitud=idSol)

        solAceptada = solicitud_aceptada.objects.create(
            descripcionSolicitudAceptada = desc,
            fechaSolicitudAceptada = fecha,
            presupuestoSolicitudAceptada = pre,
            cliente = cli,
        )
        solAceptada.save()
        sol.delete()

        context = {
            "mensaje": "Solicitud aceptada con exito",
        }
        return render(request, "pages/exito.html", context)


def salir(request):
    if "runCliente" in request.session:
        del request.session["runCliente"]
    elif "runEmpleado" in request.session:
        del request.session["runEmpleado"]
    return redirect("index")


def crearContratoCaso(request):
    if request.method == "POST":
        pre = request.POST["presupuesto"]
        fecha = datetime.now()
        idSol = request.POST["idSolAcep"]

        solAcep = solicitud_aceptada.objects.get(idSolicitudAceptada=idSol)

        objContrato = contrato.objects.create(
            fechaContrato = fecha,
            montoContrato = pre,
        )
        objContrato.save()
        solAcep.delete()

        fechaCaso = datetime.now()
        desc = request.POST["descSolAcep"]
        runCli = request.POST["cliente"]
        runEmp = request.session["runEmpleado"]

        cli = cliente.objects.get(runCliente=runCli)
        emp = empleado.objects.get(runEmpleado=runEmp)

        objCaso = caso.objects.create(
            fechaCaso = fechaCaso,
            descripcionCaso = desc,
            cliente = cli,
            empleado = emp,
            contrato = objContrato,
        )
        objCaso.save()

        context = {
            "mensaje": "Caso aceptado con exito",
        }
        return render(request, "pages/exito.html", context)