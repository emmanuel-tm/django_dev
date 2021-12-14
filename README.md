# Django Dev

## Pasos para poder utilizar y ejecutar el proyecto:

- En la Consola o Termina ejecutar el siguiente comando: *git clone https://github.com/emmanuel-tm/django_dev.git*.

- Una vez clonado el repositorio se deben seguir los siguientes pasos:

### 1. Correr el proyecto
Siempre en el mismo directorio del archivo *docker-compose.yml*
**$** `docker-compose up`

### 2. Correr la línea de comandos dentro del contenedor

**$** `docker exec -i -t django_dev bash`

Nos va a devolver a nuestra consola, una consola dentro del contenedor de software.


Una vez dentro ejecutamos el comando:

**$** `cd /opt/back_end/powermeter` 

### **IMPORTANTE:**
En caso de no existir la carpeta **database** a la altura del *manage.py* se debe
crear dicha carpeta ejecutando el siguiente comando: **$** `mkdir database`. De esta manera
se crea la carpeta que contendra la db del proyecto.
En caso de existir se debe omitir lo detallado arriba.

### 3. Iniciar el servidor
(Siempre dentro de nuestro contenedor de software - Comando N°2)  
Tenemos que ir a la carpeta donde se encuentra el archivo *manage.py*  

**$** `python manage.py runserver 0.0.0.0:8000`  

### 4. Ejecutar los siguientes comandos para realizar la primera migración:  

**$** `python manage.py makemigrations`

**$** `python manage.py migrate` 

### 5. Creamos un super usuario:  

**$** `python manage.py createsuperuser`

### 6. Detener la ejecución de nuestro contenedor y nuestro servidor
Tenemos que estar en la terminal que nos muestra los mensajes del servidor, tomada por el contenedor.
Tan solo con el comando `ctrl + c`  se detiene la ejecución de nuestro contenedor.  

Una forma alternativa es con el siguiente comando en la terminal del host:

**$** `docker stop django_dev`  

O también puede ser con docker-compose:
Tenemos que estar en la carpeta que contiene el archivo *docker-compose.yml* y hacer:


**$** `docker-compose down`  

- Una vez clonado el repositorio se debe ingresar a la carpeta del respositorio, y estar en la misma dirección/path que los archivos "Dockerfile" y "docker-compose.yml". Una vez ubicado allí, ejecutar los siguientes comandos (**NOTA**: se debe tener instalado docker y docker-compose en tu sistema):

    - *docker-compose up*

- Con el comando anterior ya tenemos nuestra imagen creada y el contenedor corriendo, por lo cual queda tomada la terminal. Lo siguiente es abrir una nueva terminal (sin cerrar la anterior) y entrar dentro del container(contenedor) por lo que se debe ejecutar el siguiente comando:

    - *docker exec -i -t "nombre_del_contenedor" bash*

- Ya estamos dentro del contenedor, entonces procedemos.


## Endpoint disponibles:

    - http://localhost:8000/api/save --> Se realiza un POST con los datos en formato JSON.

    - http://localhost:8000/api/get/max --> Devuelve el valor "máximo" de los datos.

    - http://localhost:8000/api/get/min --> Devuelve el valor "mínimo" de los datos.

    - http://localhost:8000/api/get/avg --> Devuelve el "promedio" de los datos.

    - http://localhost:8000/api-docs --> Devuelve un template con la documentación de todos los endpoints disponibles y sus APIs.


---
# Autor
Emmanuel Torres Molina

# Consultas
eotorresmolina@gmail.com
