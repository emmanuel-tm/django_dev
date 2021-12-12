# Take Home Assignment

## Django dev
Armar una API REST en Django con integración con Django Rest Framework que guarde
Mediciones en una base de datos relacional. Mediante un endpoint se envían las
mediciones, y mediante tres endpoints distintos se puede pedir el valor mínimo de las
mediciones, el valor máximo y el promedio.
El endpoint /save va a recibir una lista de valores en la *key* **“sensor_data”** y hay que
guardar cada valor por separado. La lista puede tener uno o más valores y los valores
pueden ser enteros o floats, positivos, negativos o cero.

Los *endpoints* para obtener el máximo, mínimo o promedio son **GET**, no reciben nada y
devuelven un **JSON** cuya key es la operación y el valor es el resultado de la operación.

La forma en que lo probaremos es haciendo múltiples **POST** de este estilo:
curl -X POST http://localhost:8000/api/save -H 'Content-Type:
application/json' -d '{"sensor_data": [1, -2, 3.2, 7]}'

Y luego hacer **GET** para obtener el valor máximo, mínimo y el promedio:
- curl http://localhost:8000/api/get/max
- curl http://localhost:8000/api/get/min
- curl http://localhost:8000/api/get/avg

Los tres casos deberían devolver un json de la forma:
{"max": 7}

## Ejemplo

- POST /api/save {"sensor_data": [3, 4, 8]} -> {"success”: "true"}
- GET /api/get/max -> {"max": 8}
- GET /api/get/min -> {"min": 3}
- POST /api/save {"sensor_data": [32]} -> {"success”: "true"}
- GET /api/get/max -> {"max": 32}
- GET /api/get/min -> {"min": 3}
- GET /api/get/avg -> {"avg": 11.75}

## Consideraciones:
- Debe estar subido a Github.
- Lo vamos a correr con el dev server de Django (python manage.py runserver).
- Usar sqlite.
- Es sin autenticación.

Además del código mandanos un texto explicando alguna decisión particular que hayas
decidido tomar, qué simplificaciones hiciste por ser un ejemplo de prueba y cómo lo harías
en el caso de contar con más tiempo y que sea un caso más real. Y cualquier otra
observación que te parezca necesaria.

## Algunas preguntas:
- ¿Qué tipo de autenticación usarías, y por qué?.
- ¿Cómo cambiaría la implementación sabiendo que con el tiempo las mediciones van
a estar en el orden de los cientos de miles?.