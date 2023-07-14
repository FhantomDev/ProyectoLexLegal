from django.contrib import admin
from .models import cliente, empleado, comuna, tipoEmpleado, boleta, pago, documento, contrato, caso, solicitud, solicitud_aceptada, diligencia

# Register your models here.
admin.site.register(empleado) 
admin.site.register(cliente) 
admin.site.register(comuna) 
admin.site.register(tipoEmpleado) 
admin.site.register(boleta) 
admin.site.register(pago) 
admin.site.register(documento) 
admin.site.register(contrato) 
admin.site.register(caso) 
admin.site.register(solicitud)
admin.site.register(solicitud_aceptada)
admin.site.register(diligencia)