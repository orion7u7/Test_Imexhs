# API Restful for Medical Image Processing Results

Esta rama contiene una API RESTful basada en Django que permite gestionar los resultados del procesamiento de imágenes médicas. Los resultados se almacenan en una base de datos PostgreSQL.


## Estructura del Proyecto

```bash
├── .venv/                      # Entorno virtual para dependencias del proyecto
├── ApiRestD/                   # Directorio principal del proyecto Django
│   ├── __pycache__/            
│   ├── __init__.py             
│   ├── asgi.py                 
│   ├── settings.py             # Configuración principal de Django
│   ├── urls.py                 # URLs del proyecto
│   ├── wsgi.py                 
├── device/                     # Aplicación 'device' para manejar los resultados
│   ├── __pycache__/            
│   ├── migrations/             
│   ├── __init__.py             
│   ├── admin.py                
│   ├── apps.py                 
│   ├── models.py               # Definición de los modelos de datos
│   ├── serializer.py           # Serializadores para la conversión a JSON
│   ├── tests.py                
│   ├── urls.py                 # URLs específicas de la aplicación 'device'
│   ├── views.py                # Vistas que manejan la lógica de los endpoints
├── README.md                   # Este archivo
├── debug.log                   # Archivo de log para depuración
├── manage.py                   # Script principal para manejar el proyecto Django
└── sample-04-json.json         # Archivo de ejemplo en JSON
```

## Requisitos
- Python 3.x
- PostgreSQL
- Django
- Django REST framework
- CoreAPI

## Inicio

- Haber instalado postgres y crear una DB llamada ``test_imexhs``

- Configura la base de datos PostgreSQL en settings.py:
    ```bash
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_imexhs',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
        }
    }

- Aplica las migraciones para crear las tablas en la base de datos:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

- Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver


## Uso de la API

Endpoints Disponibles:

- ### Crear: POST /api/elements/
    Permite crear un nuevo registro en la base de datos.

- ### Leer: GET /api/elements/
    Lista todos los registros existentes.

- ### Leer un Elemento: GET /api/elements/{id}/
    Recupera un registro específico por su ID.

- ### Actualizar: PUT /api/elements/{id}/
    Permite actualizar device_name y/o id de un registro existente.

- ### Eliminar: DELETE /api/elements/{id}/
    Elimina un registro por su ID.