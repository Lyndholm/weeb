import os

from weeb.settings.default import *

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = bool(int(os.getenv('DEBUG', 0)))

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '').split(' ')

INSTALLED_APPS.extend(
    [
        'storages',
    ]
)

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

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'weeb.s3_storage.StaticStorage'
DEFAULT_FILE_STORAGE = 'weeb.s3_storage.MediaStorage'

AWS_S3_ENDPOINT_URL = 'https://storage.yandexcloud.net'
AWS_S3_ACCESS_KEY_ID = os.getenv('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = os.getenv('AWS_S3_SECRET_ACCESS_KEY')
AWS_QUERYSTRING_AUTH = False
