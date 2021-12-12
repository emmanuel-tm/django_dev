# Import the models:
from applications.sensor_data.models import Measurement

from applications.sensor_data.api.serializers import *

from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from datetime import datetime


class SaveAPIView(APIView):
    '''
    `[METODO HTTP: POST]`
    \nVista de API Genérica-Personalizada basada en una
    \nClase que permite recibir peticiones mediante el
    \natributo request del tipo "POST".
    \n`Content-Type: 'application/json`.
    \nEjemplo de Schema:
    \n`{`
    \n` "sensor_data": [1, -2, 3.2, 7]`
    \n`}`
    '''

    # NOTE: Le indico que esta view no va a necesitar
    # ningún permiso, ninguna authenticación y que espera
    # recibir en el header del Mensaje HTTP: 
    # Content-Type: 'application/json'.
    permission_classes = []
    authentication_classes = []
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        '''
        Se sobreescribe la función asociada al método POST para 
        \nque reciba mediante el "request" los datos enviados, 
        \nen este caso por un sensor.
        \n`Content-Type: 'application/json`.
        \n`Schema:`
        \n`{`
        \n` "sensor_data": [1, -2, 3.2, 7]`
        \n`}`
        '''

        # Variable que va a contener la respuesta del mensaje
        response_message = {}

        # NOTE: Obtengo la lista con los datos enviados por el
        # sensor, y, almaceno la fecha y hora actual.
        values_list = request.data.get('sensor_data')
        today = datetime.now()
        date = today.strftime('%d-%m-%Y | %H:%M:%S')

        try:
            # En caso de que se envíe un dato vacío.
            if len(values_list) == 0:
                response_message = {'error': 'missing data'}
            
            # En caso de que se envíe un dato de un único valor.
            elif len(values_list) == 1:
                datum = Measurement.objects.create(value=values_list[0], date=date)
                datum.save()
                response_message = {'success': "true"}
            else:   
                # Itero la lista y voy almacenado los valores en el
                # modelo de la base de datos.
                for value in values_list:
                    datum = Measurement.objects.create(value=value, date=date)
                    datum.save()   
                response_message = {'success': "true"}
        except:
            response_message = {'success': "false"}
        
        return Response(data=response_message)
