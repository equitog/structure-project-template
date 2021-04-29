#Proceso de creacion de Usuarios en AD 
Bienvenido, la siguiente descripción ayudará a conocer brevemente el proceso de configuración. Para conocer el proceso
internamente se debe leer el código ingresando a app/ 
##Ejemplo
###¿Cómo se instala?
Para utilizar el proceso hacer los siguiente:
 - Clonar el repositorio en una ruta local.
 - Crear un entorno virtual con el nombre virtualenv_active_directory (Recomendado).
 - Instalar las dependencias del archivo requirements.txt en el entorno virtual.
 - Ejecutar "app_create_user.py"
###¿Cómo se usa?
  - Se puede ejecutar directamente por cmd.
  - Dentro de un archivo .bat.
  - También en el programador de tareas de windows.
  
####Compatible solo con windows
####Versión: 1.0
####Team: DK

## Envio de correo para bajas 
El proceso realiza el envio de correos al email proyectos_GestionAccesoPeru@grupokonecta.pe con el cual generar un ticket OTRs para que el equipo de Gestión de accesos pueda realizar la baja de los usuarios enviados en el cuerpo del correo.

### Jira
- [PEAP-238](http://ventanillaunicajira.ind.local/browse/PEAP-238)
- [PEAP-200](http://ventanillaunicajira.ind.local/browse/PEAP-200)

### Configuración

#### Mail
- host: servicios.grupokonecta.pe
- user: procesosautomaticos@servicios.grupokonecta.pe
- pass: ***********

#### Database (Prueba)
- host: pejcb933sql
- database: active_directory_test
- user: sa_ad
- pass: *************

#### Database (Producción)
- host: pejcb933sql
- database: active_directory_test
- user: sa_ad
- pass: ***********

#### Proceso
El archivo de ejecución es /app/sendbajas.py, para agregar una cuenta para el envio de correos utilizar el metodo `process`, este metodo recibe como parametro el código (id de la cuenta en meucci) de la cuenta y busca en la base de datos `active_directory` en la tabla `usuariosbajas` todas los registros que no tengan un envio de correo a OTRs (columna `enviootrs`).