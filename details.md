# Detalles:

## - Decisiones particulares que he decidido tomar:

- Implementar todo el proyecto basado en Django y Rest Framework dentro de un contenedor creando un servicio e imagen de Python utilizando **docker-compose** y **Dockerfile** para poder descartar problemas de compatibilidades en cuanto a los Sistemas Operativos y librerías utilizadas, de esta forma, se utiliza para el ambiente de desarrollo y prueba determinadas versiones especificadas. De esta manera se crea un contenedor aislado de mi sistema host.

- Todo el proyecto se realizó utilizando un sistema de control de versiones(GIT) utilizando como proveedor a GitHub. Además dicho proyecto fue desarrollado en un branch(rama) secundaria para todo el desarrollo, finalmente, ya terminado, se realizó un Merge Request(MR) o también conocido como "Pull Request" para unificarlo a la rama "master"

- Aprovechar el ORM que viene intregrado en Django para el manejo de los modelos, permitiendo de cierta manera, abstraerme de utilizar cursores y sintaxis SQL. Además por simplicidad, creé una única tabla o Modelo que almacena todos los datos.

- Se agregó al modelo que almacena los datos provenientes del sensor (Measurement) 2 columnas/atributos adicionales:
    - **date**: Contiene la fecha en formato: "dd-mm-yyyy" en la que llegaron y fueron almacenados los datos provenientes del sensor.
    - **time**: Contiene la hora en formato: "hh:mm:ss" en la que llegaron y fueron almacenados los datos provenientes del sensor.
El objetivo de agregar dichas columnas en el modelo fue para que si en el futuro, el proyecto crece, pueda agregarse más endpoints y retornar JSON que contemplen por ejemplo el *Máx*, el *Mín*, el *Avg* de los datos de una determinada fecha, poder observar la cantidad de datos de una fecha en particular, etc.

- Registré mi modelo "Measurement" para que aparezca en el Administrador de Django setenado ciertas configuraciones asociadas, permitiendo así ver los datos almacenados.

- Crear y desarrollar un serializador para el Modelo "Measurement" para que realice la validación del flujo de datos desde y hacia los modelos. Hace de intermediario entre el Modelo y las Views.

- Estructuré las carpetas de la siguiente manera: Project --> Applications --> my_app1 --> api para que respete el patrón de diseño MVT (Modelo-Vista-Template), estando dentro de la carpeta "api" todas las vistas o views, tanto personalizadas o custom, genéricas y genéricas-personalizadas(también conocidas como mixtas o híbridas) asociadas a la aplicación, en este caso sensor_data.
De esta manera si en el futuro se desea agregar otra aplicación, por ejemplo "my_app2" iría dentro de la carpeta "applications" y a su vez, tendría su propia carpeta "api" con sus vistas.

- Contemplar en la lógica de negocio dentro de las vistas(views) casos en los cuales, por ejemplo, llegue un dato vacío(lista vacía), retornando el mensaje correspondiente. Además, en caso de ocurrir algún error, sea cual sea el motivo, es "atrapado" y se genera un mensaje de retorno dentro de la excepción, permitiendo así que no se caiga el servidor.

- Para las APIs que soporta el método HTTP: GET sobreescribí la función "get()", en vez de la función "get_queryset()" ya que me permite retornar un diccionario con datos o mensajes personalizados como respuesta. En caso de tener que retornar un objeto queryset quizás me es más factible utilizar la función "get_queryset()". 

- Por último, se creó el endpoint determinado: **/api-docs**, el cual soporta una petición HTTP: **GET** y renderiza un template (archivo HTML) que contiene la documentación de todas las APIs REST generadas en este proyecto, dividido por aplicación. Para lo anterior se utilizó **Swagger UI**.

## - Por ser un caso de Prueba realicé la siguiente simplificación:

- Asumí que es un único sensor quién envía los datos, es por eso, que creé un único Modelo que almacena todos los datos.

- Creé un solo Modelo que contiene todos las columnas/atributos pero quizás para ser más escalable, por ejemplo, si en el futuro hay más de un sensor podría crear 2 Modelos que se relacionen, mediante "foreing keys" y, que un Modelo almacene los sensores (tal como funciona un Modelo User) y que el otro modelo almacene los datos que llegan de los distintos sensores, de esta manera podría diferencia o filtrar los datos que pertenecen a determinado sensor. Dicha relación es conocida como 1:N.

## - En caso de contar con más tiempo y si se tratara de un caso más real podía implementarse lo siguiente:

- Utilizar otro motor de Base de Datos Relacional, como por ejemplo "PostgreSQL" que es un sistema más robusto y tolerante a fallas, lo cual lo hace más performante, también permite la posibilidad de estar en otro servidor y pedir ciertas credenciales para ingresar (user, password). Entonces, esto me da la posibilidad de implementarlo dentro de Docker como otro servicio, y si quisiera, utilizar el servicio "adminer" para visualizar la tabla generando así un ecosistema dentro de Docker de varios microservicios.

- Podría utilizarse un método de **autenticación** y **permisos** para la consulta de la información y el envío de los datos (método HTTP: POST) que realiza el usuario, en este caso, es el sensor quien actúa como usuario y se conecta a nuestro recurso(endpoint), de esta manera, se le pediría ciertas credenciales a dicho sensor para que pueda enviar la información hacia nuestro servicio.

- Utilizaría un sistema de generación de **logging** para que quede registrado todo lo que está sucediendo entre el usuario y el servidor, por si ocurre algún error o problema inesperado. De esta manera se generan archivos que pueden ser vistos sin requerir conexión a internet(Post-Mortem).

- Finalmente se podría crear una tarea(task) que sea asincrónica, es decir, sin intervención del usuario que permita cada cierto tiempo eliminar los campos dentro de la tabla que sean los más antigüos según fecha, por ejemplo si se tiene datos que llevan varios meses, y, si quizás ya no son necesarios, eliminarlos. Esto último depende la aplicación, pero es útil cuando se tiene una cantidad masiva de datos.

## - Respuesta a las Preguntas:

- El tipo de autenticación y permisos que utilizaría (aprovechando los módulos que vienen integrados en Django y Django Rest Framework) es el de "IsAuthenticated" que permite ingresar a los recursos mediante los endpoints siempre y cuando estemos Autenticados. Entonces, primero generaría un endpoint que permita crear Token de Seguridad(de manera automática) para eso se haría uso de la función "authenticate", el cual solicitará credenciales(user y password) de acceso, para lo cual se necesita haber creado previamente un usuario (podría usarse el modelo User integrado en Django). Si dicho usuario ya fue creado, entonces la autenticación será exitosa y se procederá a crear el Token el cual queda almacenado en el Modelo "Token" que viene integrado en Django. En caso de que el usuario no se haya registrado se retornaría un mensaje, por ejemplo, de "credenciales inválidas".
Una vez obtenido, el Token el usuario(en este caso el/los sensores) podrían utilizar nuestros recursos o incluso ingresar datos mediante una petición POST.

- En el caso de que las mediciones, con el tiempo, se vuelvan en el orden de los cientos de miles de datos, podría implementarse como dije más arriba una tarea "asincrónica" que elimine aquellos datos que sean lo más antigüos, siempre y cuando ya no sean de utilidad, de esta manera, el Modelo contempla solo los datos de utilidad y más recientes. En cuanto a la antigüedad depende de la aplicación y que tipo de información representen dichos datos.

## - NOTA:

 - En el archivo **README.md** se encuentra los pasos que se deben seguir para poder correr y probar el proyecto.

## - Autor:
 - **Emmanuel Torres Molina**