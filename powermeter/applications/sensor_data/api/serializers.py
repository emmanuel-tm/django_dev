# Import the serializers:
from rest_framework import serializers

# Import the models:
from applications.sensor_data.models import *

class MeasurementSerializer(serializers.ModelSerializer):
    '''
    Clase que hereda de ModelSerializer y permite setear
    los serializadores para mi Modelo 'Measurement'.
    '''
    class Meta:
        model = Measurement
        fields = ('value', 'date')