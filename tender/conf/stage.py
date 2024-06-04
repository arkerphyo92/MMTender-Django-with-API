from .common import *

from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG") #To get the debug of env file
PRODUCTION = os.environ.get("PRODUCTION")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_URL = '/static/'
MEDIA_URL = '/tenders/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
    os.path.join(BASE_DIR, 'tendersfiles'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'tendersfiles')
