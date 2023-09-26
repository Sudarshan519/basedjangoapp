"""
Django settings for basedjangoapp project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
 
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xcd&1ctm1(l@xxl=$$=h$$d-i=*%q)%!h&2s+#zpt79&lm&y0i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app','127.0.0.1','192.168.0.50','192.168.1.99']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'baseapp',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'banners',
    'userr',
    'website',
     'corsheaders',
     'streaming_app',
     'subscription',
     'hotel_booking',
     'videouploadpp'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "whitenoise.middleware.WhiteNoiseMiddleware",
    # "django.middleware.cache.FetchFromCacheMiddleware",
    
]

ROOT_URLCONF = 'basedjangoapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'basedjangoapp.wsgi.application'
import os
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
    
#     'default':
        
#         {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get("POSTGRES_DATABASE"),
#         'USER': os.environ.get("POSTGRES_USER"),
#         'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
#         'HOST': os.environ.get("POSTGRES_HOST"),
#         'PORT': os.environ.get("POSTGRES_PORT"),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
# STATIC_URL = "/static/"
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),

    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# else:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]
# STATIC_ROOT = ''

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"), # your static/ files folder
# ]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.db.DatabaseCache",
#         "LOCATION": "my_cache_table",
#     }
# }

# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#     'PAGE_SIZE': 100
# }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
         'rest_framework.authentication.BasicAuthentication',
          'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
     'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],

        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],
}
AUTH_USER_MODEL = 'userr.CustomUser' # Add this