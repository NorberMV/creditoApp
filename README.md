# Tu crédito Web App 
Es una aplicación web basada en el framework para aplicaciones web de Python, Django que permite crear, listar y actualizar información de los usuarios del sistema. Tiene integrada una base de datos en PostgresQL administrada por AWS RDS.

### Diagrama Modelo Base de Datos del Sistema

<img src="https://github.com/NorberMV/darien_test/blob/master/modelo_BaseDatos.png" width="700">


## Contenido
* [Tu crédito Web App](#Tu-crédito-Web-App)
* [Tecnologias](#tecnologias)
* [Setup](#setup)
* [Uso](#uso)


# Tecnologias

El proyecto emplea los siguientes módulos de Python:

* Django==3.2.6
* Pillow==8.3.1
* psycopg2-binary==2.9.1
* pytz==2021.1
* sqlparse==0.4.1


## Setup

>> Clonar el repositorio de GiHub.

```python
# To run locally
# Crear el virtual Environment e instalar el archivo requirements.txt
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt

```

>> Configurar las variables de entorno en el SO adjuntas en el archivo secrets.txt
 para la configuración del endpoint de Postgres en AWS.

```python
# Ejecutar las migraciones a la Base de datos PostgresQL
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
>> Crear un superusuario para acceder como administrador

```python

python manage.py createsuperuser
# Crear usuario y contraseña
```

>> Correr el servidor de desarrollo

```python

python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Django version 3.2.6, using settings 'tucredito_site.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```


## Uso

>> Ir al panel de administración http://127.0.0.1:8000/admin/
>> Acceder con como administrador
>> Desde 'Bancos' crear los bancos correspondientes.

<img src="https://github.com/NorberMV/darien_test/blob/master/fotos/admin.png" width="600">



>> Luego ir a la url http://127.0.0.1:8000/crear-clientes/  , la cual nos permite crear y registrar información de clientes.

<img src="https://github.com/NorberMV/darien_test/blob/master/fotos/crear.png" width="600">


>> Podemos luego dar clic en 'Listar Clientes' el cual nos llevará a la url http://127.0.0.1:8000/lista-clientes/ , una vez aquí podremos ver la lista de los  clientes existentes en la base de datos.

<img src="https://github.com/NorberMV/darien_test/blob/master/fotos/lista.png" width="600">


>> Podremos dar clic en el nombre del usuario deseado para actualizar su información ó eliminarlo de la base de datos.

<img src="https://github.com/NorberMV/darien_test/blob/master/fotos/crear_eliminar.png" width="600">



Author: Norberto Moreno | 2021