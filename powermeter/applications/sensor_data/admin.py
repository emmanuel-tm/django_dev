from django.contrib import admin

# Import my models:
from applications.sensor_data.models import *

# Register your models here.
@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    '''
    Clase para registrar mi modelo 'Measurement' para
    que pueda ser utilizado desde el admin de Django.
    '''

    # Filtro por el atributo 'date'.
    list_filter = ['date']

    # Permito que se realicen búsqueda por date(fechas).
    search_fields = ['date']

    # Campos que deseo mostrar y aquellos que quiero que
    # estén ocultos, pero se puedan acceder mediante
    # el botón "Opciones Avanzadas".
    fieldsets = (
        (None, {
            'fields': ('value', 'date')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('time',),
        }),
    )

