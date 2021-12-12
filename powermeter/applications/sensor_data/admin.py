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
    pass

