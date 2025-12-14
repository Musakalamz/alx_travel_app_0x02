# ALX Travel App

A Django-based travel listing platform with REST API and comprehensive documentation.

## Features

- Django REST Framework for API development
- MySQL database integration
- Swagger/OpenAPI documentation
- CORS headers configuration
- Environment variable management
- Celery integration for background tasks
- Comprehensive API documentation at `/swagger/`

## Prerequisites

- Python 3.8+
- MySQL 5.7+
- Git

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/alx_travel_app.git
cd alx_travel_app
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your database credentials and other settings
```

5. Set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

## API Documentation

- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/
- Admin Interface: http://localhost:8000/admin/

## Project Structure

Musakalamz
Copy
Delete
Querying Power
Python Generators
Milestone 1
How PLDs Work (Step-by-Step) - Get it started!
Milestone 1: Setup and Database Configuration
Milestone 1: Setup and Database Configuration
Weight: 1
Project will start Oct 27, 2025 12:00 AM, must end by Nov 3, 2025 12:00 AM
Manual QA review must be done (request it when you are done with the project)
About the Project
The alxtravelapp project is a real-world Django application that serves as the foundation for a travel listing platform. This milestone focuses on setting up the initial project structure, configuring a robust database, and integrating tools to ensure API documentation and maintainable configurations. The aim is to equip learners with industry-standard best practices for starting and managing Django-based projects efficiently.
This milestone will teach you to set up a scalable backend, integrate MySQL for database management, and use Swagger for automated API documentation. These foundational steps are critical in preparing the application for future features and seamless team collaboration.
Learning Objective
As a professional developer, this task will enable you to:
Master Advanced Project Initialization:
Learn to bootstrap Django projects with modular, production-ready configurations.
Employ environment variable management for secure and scalable settings.
Integrate Key Developer Tools:
Set up and use Swagger (via drf-yasg) for API documentation.
Implement CORS headers and MySQL configurations for robust API interactions.
Collaborate Effectively Using Git:
Structure your projects for team collaboration with a version-controlled setup.
Adopt Industry Best Practices:
Follow best practices in managing dependencies, database configurations, and application structure.
Requirements
To successfully complete this milestone, ensure you meet the following prerequisites:
Familiarity with Django and Django REST Framework.
Knowledge of MySQL and database management.
Understanding of version control using Git.
A basic grasp of environment variable management using django-environ.
Key Highlights
Project Initialization:
Create a Django project named alxtravelapp.
Add an app named listings to encapsulate core functionalities.
Dependency Management:
Install essential packages:
django: Core framework for application development.
djangorestframework: REST API development.
django-cors-headers: Cross-Origin Resource Sharing setup.
drf-yasg: Swagger API documentation.
celery and rabbitmq: For future task queuing and background processes.
Settings Configuration:
Use django-environ to securely handle environment variables in .env files.
Configure MySQL as the primary database, ensuring proper connection handling in settings.py.
Set up REST framework and CORS headers for API support.
Swagger Integration:
Integrate Swagger for comprehensive API documentation.
Ensure all APIs are automatically documented and accessible at /swagger/.
Version Control and Submission:
Initialize a Git repository and commit all project setup files.
Push your code to a GitHub repository named alxtravelapp with the specified structure.
Additional Resources
Build a CRUD API
Django Best Practices
Manage settings securely
Integrating drf-yasg for Swagger
📝 Project Assessment (Hybrid)
Your project will be evaluated primarily through manual reviews. To ensure you receive your full score, please:
✅ Complete your project on time
📄 Submit all required files
🔗 Generate your review link
👥 Have your peers review your work
An auto-check will also be in place to verify the presence of core files needed for manual review.
⏰ Important Note
If the deadline passes, you won’t be able to generate your review link—so be sure to submit on time!
We’re here to support your learning journey. Happy coding! ✨
Tasks 0. Django Project Setup with API Documentation and Database Configuration
mandatory
Objective
Set up the Django project with the necessary dependencies, configure the database, and add Swagger for API documentation.
Instructions
Create a Django Project:
Set up a new Django project named alx_travel_app.
Create an app within the project named listings.
Install necessary packages, including django, djangorestframework, django-cors- headers, celery, rabbitmq, and drf-yasg for Swagger documentation.
Configure Settings:
In settings.py, configure the project for REST framework and CORS headers.
Set up the database configuration to use MYSQL. Use environment variables for sensitive information such as database credentials. (Hint: Use the django-environ package to handle .env files).
Add Swagger:
Install drf-yasg for Swagger documentation.
Configure Swagger to automatically document all APIs. The documentation should be available at /swagger/.
Initialize Git Repository:
Initialize a Git repository and make your initial commit with the project setup files.
Repo:
GitHub repository: alx_travel_app
Directory: alx_travel_app
File: alx_travel_app/requirement.txt, alx_travel_app/listings, alx_travel_app/settings.py, alx_travel_app/urls.py

1. Manual Review
   mandatory
   Repo:
   GitHub repository: alx_travel_app
   Directory: alx_travel_app  
   Trae
   I'll help you set up the Django travel app project according to the specifications. Let me start by creating a comprehensive todo list to track our progress.

Let me start by examining the current directory structure and then proceed with setting up the Django project.

alx_travel_app
Perfect! The directory is empty, so we can start fresh. Let me begin by creating the Django project and installing the required dependencies.

First, let's create the Django project:

Bash

Run
django-admin startproject alx_travel_app .
Let me start by creating the Django project structure. First, I'll create the requirements.txt file with all the necessary dependencies:

requirements.txt

Success
django>=4.2.0djangorestframework>=3.14.0django-cors-headers>=4.0.0drf-yasg>=1.21.0django-environ>=0.10.0celery>=5.3.0mysqlclient>=2.2.0
Now let me create the main Django project structure. I'll start by creating the manage.py file and the main project directory:

manage.py

Failed
#!/usr/bin/env python"""Django's command-line utility for administrative tasks."""import osimport sysdef main(): """Run administrative tasks.""" os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings') try: from django.core.management import execute_from_command_line except ImportError as exc: raise ImportError( "Couldn't import Django. Are you sure it's installed and " "available on your PYTHONPATH environment variable? Did you " "forget to activate a virtual environment?" ) from exc execute_from_command_line(sys. argv)if **name** == '**main**': main()
Now let me create the main project directory and its files:

asgi.py

Success
"""ASGI config for alx_travel_app project.It exposes the ASGI callable as a module-level variable named `application`.For more information on this file, seehttps://docs.djangoproject.com/en/4.2/howto/deployment/asgi/"""import osfrom django.core.asgi import get_asgi_applicationos.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')application = get_asgi_application()
wsgi.py

Success
"""WSGI config for alx_travel_app project.It exposes the WSGI callable as a module-level variable named `application`.For more information on this file, seehttps://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/"""import osfrom django.core.wsgi import get_wsgi_applicationos.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')application = get_wsgi_application()
Now let me create the main settings.py file with all the required configurations:

settings.py

Success
"""Django settings for alx_travel_app project.Generated by 'django-admin startproject' using Django 4.2.For more information on this file, seehttps://docs.djangoproject.com/en/4.2/topics/settings/For the full list of settings and their values, seehttps://docs.djangoproject.com/en/4.2/ref/settings/"""import environfrom pathlib import Path# Build paths inside the project like this: BASE_DIR / 'subdir'.BASE_DIR = Path(**file**).resolve().parent.parent# Initialize environment variablesenv = environ.Env( # Set casting, default value DEBUG=(bool, False))# Take environment variables from .env fileenviron.Env.read_env(BASE_DIR / '.env')# Quick-start development settings - unsuitable for production# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/# SECURITY WARNING: keep the secret key used in production secret!SECRET_KEY = env('SECRET_KEY', default='django-insecure-change-me-in-production')# SECURITY WARNING: don't run with debug turned on in production!DEBUG = env('DEBUG', default=True)ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])# Application definitionDJANGO_APPS = [ 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles',]THIRD_PARTY_APPS = [ 'rest_framework', 'corsheaders', 'drf_yasg',]LOCAL_APPS = [ 'listings',]INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPSMIDDLEWARE = [ 'corsheaders.middleware. CorsMiddleware', 'django.middleware.security. SecurityMiddleware', 'django.contrib.sessions. middleware.SessionMiddleware', 'django.middleware.common. CommonMiddleware', 'django.middleware.csrf. CsrfViewMiddleware', 'django.contrib.auth.middleware. AuthenticationMiddleware', 'django.contrib.messages. middleware.MessageMiddleware', 'django.middleware.clickjacking. XFrameOptionsMiddleware',]ROOT_URLCONF = 'alx_travel_app.urls'TEMPLATES = [ { 'BACKEND': 'django.template. backends.django. DjangoTemplates', 'DIRS': [], 'APP_DIRS': True, 'OPTIONS': { 'context_processors': [ 'django.template. context_processors. debug', 'django.template. context_processors. request', 'django.contrib. auth. context_processors. auth', 'django.contrib. messages. context_processors. messages', ], }, },]WSGI_APPLICATION = 'alx_travel_app.wsgi.application'# Database# https://docs.djangoproject.com/en/4.2/ref/settings/#databasesDATABASES = { 'default': { 'ENGINE': 'django.db. backends.mysql', 'NAME': env('DB_NAME', default='alx_travel_app'), 'USER': env('DB_USER', default='root'), 'PASSWORD': env ('DB_PASSWORD', default=''), 'HOST': env('DB_HOST', default='localhost'), 'PORT': env('DB_PORT', default='3306'), 'OPTIONS': { 'init_command': "SET sql_mode='STRICT_TRANS_T ABLES'", }, }}# Password validation# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validatorsAUTH_PASSWORD_VALIDATORS = [ { 'NAME': 'django.contrib. auth.password_validation. UserAttributeSimilarityValid ator', }, { 'NAME': 'django.contrib. auth.password_validation. MinimumLengthValidator', }, { 'NAME': 'django.contrib. auth.password_validation. CommonPasswordValidator', }, { 'NAME': 'django.contrib. auth.password_validation. NumericPasswordValidator', },]# Internationalization# https://docs.djangoproject.com/en/4.2/topics/i18n/LANGUAGE_CODE = 'en-us'TIME_ZONE = 'UTC'USE_I18N = TrueUSE_TZ = True# Static files (CSS, JavaScript, Images)# https://docs.djangoproject.com/en/4.2/howto/static-files/STATIC_URL = 'static/'STATIC_ROOT = BASE_DIR / 'staticfiles'# Default primary key field type# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-fieldDEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'# Django REST Framework ConfigurationREST_FRAMEWORK = { 'DEFAULT_AUTHENTICATION_CLASSES' : [ 'rest_framework. authentication. SessionAuthentication', 'rest_framework. authentication. TokenAuthentication', ], 'DEFAULT_PERMISSION_CLASSES': [ 'rest_framework.permissions. IsAuthenticatedOrReadOnly', ], 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination. PageNumberPagination', 'PAGE_SIZE': 20, 'DEFAULT_RENDERER_CLASSES': [ 'rest_framework.renderers. JSONRenderer', 'rest_framework.renderers. BrowsableAPIRenderer', ],}# CORS ConfigurationCORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', default=[ "http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:8000", "http://127.0.0.1:8000",])CORS_ALLOW_CREDENTIALS = TrueCORS_ALLOWED_HEADERS = [ 'accept', 'accept-encoding', 'authorization', 'content-type', 'dnt', 'origin', 'user-agent', 'x-csrftoken', 'x-requested-with',]# Swagger SettingsSWAGGER_SETTINGS = { 'SECURITY_DEFINITIONS': { 'Token': { 'type': 'apiKey', 'name': 'Authorization', 'in': 'header' } }, 'USE_SESSION_AUTH': False, 'JSON_EDITOR': True, 'SUPPORTED_SUBMIT_METHODS': [ 'get', 'post', 'put', 'delete', 'patch' ], 'OPERATIONS_SORTER': 'alpha', 'TAGS_SORTER': 'alpha', 'DOC_EXPANSION': 'none', 'DEEP_LINKING': True, 'SHOW_EXTENSIONS': True, 'SHOW_COMMON_EXTENSIONS': True,}REDOC_SETTINGS = { 'LAZY_RENDERING': False,}# Celery Configuration (for future use)CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='pyamqp://guest@localhost//')CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', default='rpc://')CELERY_ACCEPT_CONTENT = ['application/json']CELERY_TASK_SERIALIZER = 'json'CELERY_RESULT_SERIALIZER = 'json'CELERY_TIMEZONE = TIME_ZONE
Now let me create the main URLs configuration with Swagger integration:

urls.py

Success
"""URL configuration for alx_travel_app project.The `urlpatterns` list routes URLs to views. For more information please see: https://docs.djangoproject.com/ en/4.2/topics/http/urls/Examples:Function views 1. Add an import: from my_app import views 2. Add a URL to urlpatterns: path('', views.home, name='home')Class-based views 1. Add an import: from other_app.views import Home 2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')Including another URLconf 1. Import the include() function: from django.urls import include, path 2. Add a URL to urlpatterns: path('blog/', include('blog. urls'))"""from django.contrib import adminfrom django.urls import path, include, re_pathfrom rest_framework import permissionsfrom drf_yasg.views import get_schema_viewfrom drf_yasg import openapi# Swagger/OpenAPI Schema Configurationschema_view = get_schema_view( openapi.Info( title="ALX Travel App API", default_version='v1', description="A comprehensive travel listing platform API", terms_of_service="https:// www.google.com/policies/ terms/", contact=openapi.Contact (email="contact@alxtravelapp .local"), license=openapi.License (name="BSD License"), ), public=True, permission_classes=(permissions. AllowAny,),)urlpatterns = [ # Admin interface path('admin/', admin.site.urls), # API endpoints path('api/v1/', include ('listings.urls')), # API Documentation path('swagger<format>/', schema_view.without_ui (cache_timeout=0), name='schema-json'), path('swagger/', schema_view. with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), path('redoc/', schema_view. with_ui('redoc', cache_timeout=0), name='schema-redoc'), # API Root re_path(r'^api/v1/', include ('rest_framework.urls', namespace='rest_framework')),]
Now let me create the listings app structure:

apps.py

Success
from django.apps import AppConfigclass ListingsConfig(AppConfig): default_auto_field = 'django.db. models.BigAutoField' name = 'listings'
admin.py

Success
from django.contrib import admin# Register your models here.
models.py

Success
from django.db import models# Create your models here.
views.py

Success
from django.shortcuts import renderfrom rest_framework.decorators import api_viewfrom rest_framework.response import Responsefrom rest_framework import statusfrom drf_yasg.utils import swagger_auto_schemafrom drf_yasg import openapi# Create your views here.@swagger_auto_schema( method='get', operation_description="Welcome endpoint for the ALX Travel App API", responses={ 200: openapi.Response( description="Welcome message", examples={ "application/json": { "message": "Welcome to ALX Travel App API", "version": "v1", "status": "active" } } ) })@api_view(['GET'])def welcome_view(request): """ Welcome endpoint for the ALX Travel App API """ return Response({ "message": "Welcome to ALX Travel App API", "version": "v1", "status": "active" }, status=status.HTTP_200_OK)
urls.py

Success
from django.urls import pathfrom . import viewsapp_name = 'listings'urlpatterns = [ path('', views.welcome_view, name='welcome'),]
tests.py

Success
from django.test import TestCase# Create your tests here.
Now let me create the .env template file:

.env.example

Success

# Django SettingsSECRET_KEY=your-secret-key-hereDEBUG=TrueALLOWED_HOSTS=localhost,127.0.0.1# Database ConfigurationDB_NAME=alx_travel_appDB_USER=rootDB_PASSWORD=your-mysql-passwordDB_HOST=localhostDB_PORT=3306# CORS ConfigurationCORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000# Celery ConfigurationCELERY_BROKER_URL=pyamqp://guest@localhost//CELERY_RESULT_BACKEND=rpc://

Let me also create a basic .env file for development:

.env

Success

# Django SettingsSECRET_KEY=django-insecure-development-key-change-in-productionDEBUG=TrueALLOWED_HOSTS=localhost,127.0.0.1# Database ConfigurationDB_NAME=alx_travel_appDB_USER=rootDB_PASSWORD=DB_HOST=localhostDB_PORT=3306# CORS ConfigurationCORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000# Celery ConfigurationCELERY_BROKER_URL=pyamqp://guest@localhost//CELERY_RESULT_BACKEND=rpc://

Now let me create a .gitignore file:

.gitignore

Success

# Byte-compiled / optimized / DLL files**pycache**/_.py[cod]_$py.class# C extensions*.so# Distribution / packaging.Pythonbuild/develop-eggs/dist/downloads/eggs/.eggs/lib/lib64/parts/sdist/var/wheels/pip-wheel-metadata/share/python-wheels/*.egg-info/.installed.cfg*.eggMANIFEST# PyInstaller# Usually these files are written by a python script from a template# before PyInstaller builds the exe, so as to inject date/other infos into it.*.manifest*.spec# Installer logspip-log.txtpip-delete-this-directory.txt# Unit test / coverage reportshtmlcov/.tox/.nox/.coverage.coverage.*.cachenosetests.xmlcoverage.xml*.cover*.py,cover.hypothesis/.pytest*cache/# Translations*.mo*.pot# Django stuff:*.loglocal_settings.pydb.sqlite3db.sqlite3-journal# Flask stuff:instance/.webassets-cache# Scrapy stuff:.scrapy# Sphinx documentationdocs/\_build/# PyBuildertarget/# Jupyter Notebook.ipynb_checkpoints# IPythonprofile_default/ipython_config.py# pyenv.python-version# pipenv# According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.# However, in case of collaboration, if having platform-specific dependencies or dependencies# having no cross-platform support, pipenv may install dependencies that don't work, or not# install all needed dependencies.#Pipfile.lock# PEP 582; used by e.g. github.com/David-OConnor/pyflow**pypackages**/# Celery stuffcelerybeat-schedulecelerybeat.pid# SageMath parsed files*.sage.py# Environments.env.venvenv/venv/ENV/env.bak/venv.bak/# Spyder project settings.spyderproject.spyproject# Rope project settings.ropeproject# mkdocs documentation/site# mypy.mypy_cache/.dmypy.jsondmypy.json# Pyre type checker.pyre/# IDE.vscode/.idea/*.swp*.swo\*~# OS.DS_Store.DS_Store?.*\*.Spotlight-V100.Trashesehthumbs.dbThumbs.db# Media filesmedia/# Static filesstaticfiles/

Now let me create a README.md file to document the project:

README.md

Success

# ALX Travel AppA Django-based travel listing platform with REST API and comprehensive documentation.## Features- Django REST Framework for API development- MySQL database integration- Swagger/OpenAPI documentation- CORS headers configuration- Environment variable management- Celery integration for background tasks- Comprehensive API documentation at `/swagger/`## Prerequisites- Python 3.8+- MySQL 5.7+- Git## Installation1. Clone the repository:`bashgit clone https://github.com/yourusername/alx_travel_app.gitcd alx_travel_app`2. Create a virtual environment:`bashpython -m venv venvsource venv/bin/activate  # On Windows: venv\Scripts\activate`3. Install dependencies:`bashpip install -r requirements.txt`4. Set up environment variables:`bashcp .env.example .env# Edit .env with your database credentials and other settings`5. Set up the database:`bashpython manage.py makemigrationspython manage.py migrate`6. Create a superuser:`bashpython manage.py createsuperuser`7. Run the development server:`bashpython manage.py runserver`## API Documentation- Swagger UI: http://localhost:8000/swagger/- ReDoc: http://localhost:8000/redoc/- Admin Interface: http://localhost:8000/admin/## Project Structure

alx_travel_app/ ├── alx_travel_app/ # Main project directory │ ├── init.py │ ├── settings.py # Django settings with environment variables │ ├── urls.py # Main URL configuration with Swagger │ ├── wsgi.py │ └── asgi.py ├── listings/ # Listings app │ ├── init.py │ ├── admin.py │ ├── apps.py │ ├── models.py │ ├── views.py │ ├── urls.py │ └── tests.py ├── requirements.txt # Project dependencies ├── manage.py # Django management script ├── .env.example # Environment variables template ├── .gitignore # Git ignore file └── README.md # This file

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=alx_travel_app
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306

CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Milestone 2: Creating Models, Serializers, and Seeders

This milestone adds relational models, DRF serializers, and a seeding command.

### Added

- Models: `Listing`, `Booking`, `Review` with relationships and validations.
- Serializers: `ListingSerializer`, `BookingSerializer`.
- Seeder: `python manage.py seed` (with `--count N`).

### Usage

1. Apply migrations:
   - `python manage.py makemigrations listings`
   - `python manage.py migrate`
2. Seed sample listings:
   - `python manage.py seed` or `python manage.py seed --count 25`
3. Swagger docs:
   - `http://localhost:8000/swagger/`

### Notes

- `Booking.total_price` is computed from nights × price per night.
- `Review.rating` enforces 1–5 range; users can review a listing once.
