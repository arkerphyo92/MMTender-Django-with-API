import os
from .common import *
import dj_database_url
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = False
PRODUCTION = 0
ALLOWED_HOSTS = [
  'localhost',
  '127.0.0.1',
]


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    "default" : dj_database_url.parse("postgres://mmtender_database_user:F6sse1vE5tLNpwh9coZEoQEjzXTcmfxW@dpg-cpfj61tds78s739e3540-a.singapore-postgres.render.com/mmtender_database")
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# if not DEBUG:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
#     STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#     MEDIA_ROOT = os.path.join(BASE_DIR, 'tendersfiles')
#     MEDIAFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = 'static/'
MEDIA_URL = 'tenders/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
    os.path.join(BASE_DIR, 'tenders/'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'tendersfiles/')


# Log file Checker

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'django_debug.log',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    },
}
