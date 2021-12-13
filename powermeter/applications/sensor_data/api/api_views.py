# Import the models and serializers:
from django.contrib.auth import authenticate
from rest_framework import permissions
from applications.sensor_data.models import Measurement
from applications.sensor_data.api.serializers import *

# Import the permissions, parsers and response:
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

# Import Class-based Views:
from rest_framework.views import APIView

# Import aggregation functions:
from django.db.models import Max, Min, Avg

from datetime import datetime


class SaveAPIView(APIView):
    '''
    `[METODO HTTP: POST]`
    \nVista de API Genérica-Personalizada(Hybrid) basada
    \nen una Clase que permite recibir peticiones mediante el
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
        \n`Ejemplo de Schema de Entrada:`
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
        date = today.strftime('%d-%m-%Y')
        time = today.strftime('%H:%M:%S')
        print(time)

        try:
            # En caso de que se envíe un dato vacío.
            if len(values_list) == 0:
                response_message = {'error': 'missing data'}
            
            # En caso de que se envíe un dato de un único valor.
            elif len(values_list) == 1:
                datum = Measurement.objects.create(value=values_list[0], 
                                                    date=date,
                                                    time=time)
                datum.save()
                response_message = {'success': "true"}
            else:   
                # Itero la lista y voy almacenado los valores en el
                # modelo de la base de datos.
                for value in values_list:
                    datum = Measurement.objects.create(value=value, 
                                                        date=date,
                                                        time=time)
                    datum.save()   
                response_message = {'success': "true"}
        except:
            response_message = {'success': "false"}
        
        return Response(data=response_message)


class GetMaxAPIView(APIView):
    '''
    `[METODO HTTP: GET]`
    \nVista de API Genérica-Personalizada(Hybrid) basada
    \nen una Clase que permite recibir peticiones mediante el
    \natributo request del tipo "GET".
    \nRetorna el valor "MÁXIMO" de los datos.
    \n`Ejemplo de Schema de Retorno Exitoso:`
    \n`{`
    \n` "max": 29`
    \n`}`
    '''

    # NOTE: Le indico que esta view no va a necesitar
    # ningún permiso ni authenticación. Se le asigna
    # el serializador para la validación del flujo 
    # de datos desde y hacia la Base de Datos.
    permissions_classes = []
    authentications_classes = []
    serializer = MeasurementSerializer

    def get(self, request, format=None):
        '''
        \nSe sobreescribe la función asociada el método GET para
        \nretornar el valor "Máximo" de los datos presentes
        \nen la Base de Datos.
        \n`Ejemplo de Schema de Retorno Exitoso:`
        \n`{`
        \n` "max": 29`
        \n`}`
        '''
        max_value = dict()

        try:
            # NOTE: obtengo el valor máximo del diccionario de 
            # la columna 'value'.
            queryset = Measurement.objects.aggregate(Max('value'))
            value = queryset.get('value__max')

            # En caso de que no haya ningún valor almacenado en la
            # Base de Datos.
            if queryset == {}:
                max_value = {'max': 'NaN'}
            else:
                # NOTE: se realiza lo siguiente para saber si el valor
                # máximo retornado es entero o si es flotante.
                # En caso de ser entero se devuelve como un valor
                # entero. Esto se hace comprobando si la parte decimal
                # es igual a 0.
                if float(str(value).split('.')[1]) == 0:
                    value = int(value)

                max_value = {'max': value}
        except:
            max_value = {'max': 'NaN'}

        return Response(data=max_value)


class GetMinAPIView(APIView):
    '''
    `[METODO HTTP: GET]`
    \nVista de API Genérica-Personalizada(Hybrid) basada
    \nen una Clase que permite recibir peticiones mediante el
    \natributo request del tipo "GET".
    \nRetorna el valor "Mínimo" de los datos.
    \n`Ejemplo de Schema de Retorno Exitoso:`
    \n`{`
    \n` "min": -14.98`
    \n`}`
    '''

    # NOTE: Le indico que esta view no va a necesitar
    # ningún permiso ni authenticación. Se le asigna
    # el serializador para la validación del flujo 
    # de datos desde y hacia la Base de Datos.
    permissions_classes = []
    authentications_classes = []
    serializer = MeasurementSerializer

    def get(self, request, format=None):
        '''
        \nSe sobreescribe la función asociada el método GET para
        \nretornar el valor "MINIMO" de los datos presentes
        \nen la Base de Datos.
        \n`Ejemplo de Schema de Retorno Exitoso:`
        \n`{`
        \n` "min": -14.98`
        \n`}`
        '''
        min_value = dict()

        try:
            # NOTE: obtengo el valor máximo del diccionario de 
            # la columna 'value'.
            queryset = Measurement.objects.aggregate(Min('value'))
            value = queryset.get('value__min')

            # En caso de que no haya ningún valor almacenado en la
            # Base de Datos.
            if queryset == {}:
                min_value = {'min': 'NaN'}
            else:
                # NOTE: se realiza lo siguiente para saber si el valor
                # máximo retornado es entero o si es flotante.
                # En caso de ser entero se devuelve como un valor
                # entero. Esto se hace comprobando si la parte decimal
                # es igual a 0.
                if float(str(value).split('.')[1]) == 0:
                    value = int(value)

                min_value = {'min': value}
        except:
            min_value = {'min': 'NaN'}

        return Response(data=min_value)


class GetAvgAPIView(APIView):
    '''
    `[METODO HTTP: GET]`
    \nVista de API Genérica-Personalizada(Hybrid) basada
    \nen una Clase que permite recibir peticiones mediante el
    \natributo request del tipo "GET".
    \nRetorna el valor "Promedio" de los datos.
    \n`Ejemplo de Schema de Retorno Exitoso:`
    \n`{`
    \n` "avg": 1.28`
    \n`}`
    '''

    # NOTE: Le indico que esta view no va a necesitar
    # ningún permiso ni authenticación. Se le asigna
    # el serializador para la validación del flujo 
    # de datos desde y hacia la Base de Datos.
    permissions_classes = []
    authentications_classes = []
    serializer = MeasurementSerializer

    def get(self, request, format=None):
        '''
        \nSe sobreescribe la función asociada el método GET para
        \nretornar el valor "PROMEDIO" de los datos presentes
        \nen la Base de Datos.
        \n`Ejemplo de Schema de Retorno Exitoso:`
        \n`{`
        \n` "avg": 1.28`
        \n`}`
        '''
        min_value = dict()

        try:
            # NOTE: obtengo el valor máximo del diccionario de 
            # la columna 'value'.
            queryset = Measurement.objects.aggregate(Avg('value'))
            value = queryset.get('value__avg')

            # En caso de que no haya ningún valor almacenado en la
            # Base de Datos.
            if queryset == {}:
                avg_value = {'avg': 'NaN'}
            else:
                # NOTE: se realiza lo siguiente para saber si el valor
                # máximo retornado es entero o si es flotante.
                # En caso de ser entero se devuelve como un valor
                # entero. Esto se hace comprobando si la parte decimal
                # es igual a 0.
                if float(str(value).split('.')[1]) == 0:
                    value = int(value)

                avg_value = {'avg': round(value, 2)}    # Redondeo a 2 decimales.
        except:
            avg_value = {'avg': 'NaN'}

        return Response(data=avg_value)