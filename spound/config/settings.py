import os

from dj_database_url import parse as parse_db_url
from prettyconf import config


# Project Structure
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')

DEBUG = config('DEBUG', default=False, cast=config.boolean)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=config.list)
SECRET_KEY = config('SECRET_KEY')

# Project Info
PROJECT_NAME = 'InSpace - knowledge sharing'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(FRONTEND_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': config('TEMPLATE_DEBUG', default=DEBUG, cast=config.boolean),
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=parse_db_url),
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(FRONTEND_DIR, 'static_deploy')
STATIC_DIR = os.path.join(FRONTEND_DIR, 'static')
STATICFILES_DIRS = (
    ('css', '%s/css' % STATIC_DIR),
    ('fonts', '%s/fonts' % STATIC_DIR),
    ('images', '%s/images' % STATIC_DIR),
    ('js', '%s/js' % STATIC_DIR),
)


SPOTIFY_CLIENT_ID = config('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = config('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = config('SPOTIFY_REDIRECT_URI')
SPOTIFY_CACHE_FILE = config('SPOTIFY_CACHE_FILE')
