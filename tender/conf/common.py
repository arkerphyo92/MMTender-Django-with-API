
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'django_ckeditor_5', #Description for Add and Edit Tenders
    'rest_framework', #for api
    'debug_toolbar',
]

APPS = [
    'listings',
    'users',
    'frontend',
    'api',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + APPS

SITE_ID = 1 #Need this because 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'tender.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'tender.context_processor.project_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'tender.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Asia/Bangkok'
USE_I18N = True
USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# customColorPalette = [
#         {
#             'color': 'hsl(4, 90%, 58%)',
#             'label': 'Red'
#         },
#         {
#             'color': 'hsl(340, 82%, 52%)',
#             'label': 'Pink'
#         },
#         {
#             'color': 'hsl(291, 64%, 42%)',
#             'label': 'Purple'
#         },
#         {
#             'color': 'hsl(262, 52%, 47%)',
#             'label': 'Deep Purple'
#         },
#         {
#             'color': 'hsl(231, 48%, 48%)',
#             'label': 'Indigo'
#         },
#         {
#             'color': 'hsl(207, 90%, 54%)',
#             'label': 'Blue'
#         },
#     ]


# CKEDITOR_5_CONFIGS = {
#     'default': {
#         'toolbar': [
#             {'name': 'styles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', 'RemoveFormat']},
#             {'name': 'blocks', 'items': ['NumberedList', 'BulletedList', '-', 'Blockquote']},
#             {'name': 'links', 'items': ['Link', 'Unlink']},
#             {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#             {'name': 'tools', 'items': ['Maximize']},
#         ],
#         'height': 300,
#         'width': '100%',
#     },
# }


customColorPalette = [
        {
            'color': 'hsl(4, 90%, 58%)',
            'label': 'Red'
        },
        {
            'color': 'hsl(340, 82%, 52%)',
            'label': 'Pink'
        },
        {
            'color': 'hsl(291, 64%, 42%)',
            'label': 'Purple'
        },
        {
            'color': 'hsl(262, 52%, 47%)',
            'label': 'Deep Purple'
        },
        {
            'color': 'hsl(231, 48%, 48%)',
            'label': 'Indigo'
        },
        {
            'color': 'hsl(207, 90%, 54%)',
            'label': 'Blue'
        },
    ],


CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList'],

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', 
                    'bulletedList', 'numberedList', 
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor',],
        'skin': 'moono-dark',
    },
}

# CKEDITOR_CONFIGS = {
#     'default': {
#         'skin': 'moono',
#         'toolbar_Basic': [
#             ['-', 'Bold', 'Italic']
#         ],
#         'toolbar_YourCustomToolbarConfig': [
#             {'name': 'basicstyles',
#              'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
#             {'name': 'paragraph',
#              'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
#                        'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl' ]},
#             {'name': 'links', 'items': ['Link', 'Unlink']},
#             '/',
#             {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#             {'name': 'yourcustomtools', 'items': [
#                 # put the name of your editor.ui.addButton here
#                 'Preview',
#             ]},
#         ],
#         'toolbar': 'YourCustomToolbarConfig',
#         'tabSpaces': 4,
#         'extraPlugins': ','.join([
#             # 'uploadimage',  # Remove the upload image feature
#             # Remove any other plugins related to file or image handling
#             'div',
#             'autolink',
#             'autoembed',
#             'embedsemantic',
#             'autogrow',
#             'widget',
#             'lineutils',
#             'clipboard',
#             'dialog',
#             'dialogui',
#             'elementspath'
#         ]),
#     }
# }

CKEDITOR_UPLOAD_PATH = 'tenders/upload/'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}