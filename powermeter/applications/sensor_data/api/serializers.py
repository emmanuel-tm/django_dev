# Import the serializers:
from rest_framework import serializers

# Import the models:
from applications.sensor_data.models import *

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('value', 'date')