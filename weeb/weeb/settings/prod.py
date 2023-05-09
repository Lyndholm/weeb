import os

from weeb.settings.default import *

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = bool(int(os.getenv('DEBUG', 0)))

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(' ')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'weeb'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'password'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}
