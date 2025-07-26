import os
from pathlib import Path

# ========================
# BASE DEL PROYECTO
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent

# ========================
# SEGURIDAD Y DEBUG
# ========================
SECRET_KEY = 'tu_clave_secreta_de_django'  # ⚠️ cámbiala para producción
DEBUG = True

ALLOWED_HOSTS = ['*']  # Puedes poner tu dominio si lo subes

# ========================
# APPS INSTALADAS
# ========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contacto',  # Tu app personalizada
]

# ========================
# MIDDLEWARE
# ========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ========================
# URL ROOT Y WSGI
# ========================
ROOT_URLCONF = 'nombre_proyecto.urls'

WSGI_APPLICATION = 'nombre_proyecto.wsgi.application'

# ========================
# BASE DE DATOS
# ========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ========================
# VALIDACIÓN DE USUARIO
# ========================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]

# ========================
# LOCALIZACIÓN
# ========================
LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ========================
# RUTAS DE ARCHIVOS
# ========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ========================
# PLANTILLAS
# ========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Agrega tu carpeta de templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ========================
# CONFIGURACIÓN DE CORREO
# ========================
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "d.arrietavega@gmail.com"
EMAIL_HOST_PASSWORD = "TU_CLAVE_APP"  # 🔐 Usa una clave de aplicación de Gmail

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ========================
# CONFIG PARA JSON EN FETCH
# ========================
CORS_ALLOW_ALL_ORIGINS = True  # (para pruebas)
