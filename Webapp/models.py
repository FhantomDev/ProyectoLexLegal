from django.db import models

# Create your models here.
class comuna(models.Model):
    idComuna = models.AutoField(primary_key=True)
    nombreComuna = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombreComuna)
    

class tipoEmpleado(models.Model):
    idTipoEmpleado = models.AutoField(primary_key=True)
    nombreTipoEmpleado = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombreTipoEmpleado)


class cliente(models.Model):
    runCliente = models.CharField(max_length=10, primary_key=True)
    nombreCliente = models.CharField(max_length=20, blank=False, null=False)
    correoCliente = models.EmailField(max_length=20, blank=False, null=False)
    contraseñaCliente = models.CharField(max_length=15, blank=False, null=False)
    apPaternoCliente = models.CharField(max_length=20, blank=False, null=False)
    apMaternoCliente = models.CharField(max_length=20, blank=False, null=False)
    direccionCliente = models.CharField(max_length=20, blank=False, null=False)
    telefonoCliente = models.IntegerField(blank=False, null=False)
    comuna = models.ForeignKey("comuna", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombreCliente)+" "+str(self.apPaternoCliente)+" "+str(self.apMaternoCliente)
    

class empleado(models.Model):
    runEmpleado = models.CharField(max_length=10, primary_key=True)
    nombreEmpleado = models.CharField(max_length=20, blank=False, null=False)
    apPaternoEmpleado = models.CharField(max_length=20, blank=False, null=False)
    apMaternoEmpleado = models.CharField(max_length=20, blank=False, null=False)
    contraseñaEmpleado = models.CharField(max_length=15, blank=False, null=False)
    tipoEmpleado = models.ForeignKey("tipoEmpleado", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombreEmpleado)+" "+str(self.apPaternoEmpleado)+" "+str(self.apMaternoEmpleado)


class solicitud(models.Model):
    idSolicitud = models.AutoField(primary_key=True)
    descripcionSolicitud = models.CharField(max_length=100, blank=False, null=False)
    fechaSolicitud = models.DateField(blank=False, null=False)
    cliente = models.ForeignKey("cliente", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idSolicitud)+" "+str(self.cliente)


class solicitud_aceptada(models.Model):
    idSolicitudAceptada = models.AutoField(primary_key=True)
    descripcionSolicitudAceptada = models.CharField(max_length=100, blank=False, null=False)
    fechaSolicitudAceptada = models.DateField(blank=False, null=False)
    presupuestoSolicitudAceptada = models.IntegerField(blank=False, null=False)
    cliente = models.ForeignKey("cliente", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idSolicitudAceptada)+" "+str(self.cliente)


class contrato(models.Model):
    idContrato = models.AutoField(primary_key=True)
    fechaContrato = models.DateField(blank=False, null=False)
    montoContrato = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.idContrato)+" "+str(self.fechaContrato)


class caso(models.Model):
    idCaso = models.AutoField(primary_key=True)
    fechaCaso = models.DateField(blank=False, null=False)
    descripcionCaso = models.TextField(blank=False, null=False)
    cliente = models.ForeignKey("cliente", on_delete=models.CASCADE)
    empleado = models.ForeignKey("empleado", on_delete=models.CASCADE)
    contrato = models.ForeignKey("contrato", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idCaso)+" "+str(self.cliente)+" "+str(self.empleado)
    

class documento(models.Model):
    idDocumento = models.AutoField(primary_key=True)
    descripcionDocumento = models.CharField(max_length=20, blank=False, null=False)
    archivoDocumento = models.FileField(upload_to='documentos/')
    fechaDocumento = models.DateField(blank=False, null=False)
    caso = models.ForeignKey("caso", on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.idDocumento)+" "+str(self.descripcionDocumento)


class diligencia(models.Model):
    idDiligencia = models.AutoField(primary_key=True)
    descripcionDiligencia = models.CharField(max_length=100, blank=False, null=False)
    fechaDiligencia = models.DateField(blank=False, null=False)
    caso = models.ForeignKey("caso", on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.idDiligencia)+" "+str(self.descripcionDiligencia)


class boleta(models.Model):
    idBoleta= models.AutoField(primary_key=True)
    fechaBoleta = models.DateField(blank=False, null=False)
    montoPagoBoleta = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.idBoleta)+" "+str(self.fechaBoleta)+" "+str(self.montoPagoBoleta)
    

class pago(models.Model):
    idPago = models.AutoField(primary_key=True)
    fechaPago = models.DateField(blank=False, null=False)
    contrato = models.ForeignKey("contrato", on_delete=models.CASCADE)
    boleta = models.ForeignKey("boleta", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idPago)+" "+str(self.contrato)+" "+str(self.boleta)