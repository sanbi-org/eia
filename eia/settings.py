"""
Django settings for eia project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uehb80ww)9wg82^0b_h(ccr0hap!l_a&2!rou!h@aw8)&*-30p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'core',
    'leaflet',
    'bootstrap3',
    'django_filters',
    'mptt',

    # django allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.twitter',

    # TODO add mollom https://github.com/marconi/django-mollom
)

# django allauth
SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'eia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # django allauth
                'django.template.context_processors.request',
            ],
        },
    },
]

# django allauth
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'eia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
#}

DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'eia_tool',
         'USER': 'postgres',
         'PASSWORD': 'root',
         'PORT': '5433',
     }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

DATETIME_INPUT_FORMATS = ('%Y-%m-%d %H:%M',
                          '%d %b %Y (%A) %H:%M',
                          '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
                          '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
                          '%Y/%m/%d %H:%M',        # '2014/10/28 17:30'
                          '%Y-%m-%d',              # '2006-10-25'
                          '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
                          '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
                          '%m/%d/%Y',              # '10/25/2006'
                          '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
                          '%m/%d/%y %H:%M',        # '10/25/06 14:30'
                          '%m/%d/%y'
                          )

DATETIME_FORMAT = 'j N P'

# Allauth settings
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_FORM_CLASS = 'core.forms.SignupForm'
LOGIN_REDIRECT_URL = '/projects/'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Leaflet-django https://github.com/makinacorpus/django-leaflet
LEAFLET_CONFIG = {
    'SPATIAL_EXTENT': (15, -35, 33, -21),
    'DEFAULT_CENTER': (-29, 24.5),
    'DEFAULT_ZOOM': 5,
}

# Django-bootstrap 3 settings
BOOTSTRAP3 = {
    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-2',
    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-5'
}

# Django-admin-bootstrap
DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'
from django.contrib import messages

MESSAGE_TAGS = {
            messages.SUCCESS: 'alert-success success',
            messages.WARNING: 'alert-warning warning',
            messages.ERROR: 'alert-danger error'
}

# My own spreadsheet creation methods need this
MAX_XLSX_ROWS = 2000

# I have a taxonomy tree builder which uses these settings
GBIF_API_OFFSET = 40
GBIF_API_CHILDREN_URL = 'http://api.gbif.org/v1/species/{id}/children?limit=' + str(GBIF_API_OFFSET) + '&offset={offset}&language=en'
GBIF_API_OCCURRENCE_URL = 'http://api.gbif.org/v1/occurrence/search?taxonKey={id}&country=ZA&limit=0&language=en&basisofrecord=HUMAN_OBSERVATION' # We just want count, so limit 0
GBIF_API_SPECIES_URL = 'http://api.gbif.org/v1/species/{id}?&language=en'
BASE_TAXA = ['Chiroptera', 'Aves'] # 734 and 212 GBIF IDs
# This token ID for IUCN has been generated for SANBI's use only
IUCN_API_URL = 'http://apiv3.iucnredlist.org/api/v3/species/{name}?token=c912c913108d604744f52d5e55a0833d1abe77ffa2d2462de948d930e8f9bb90'

# Add the production settings, whatever this is should check to see if it is on production before changing settings
import sys

# Added this 12 Feb to make it openshift compatible
ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:
    ON_OPENSHIFT = True

    file = os.path.join(os.path.dirname(os.path.dirname((os.path.abspath(sys.argv[0])))), 'settings_production.py')
    file = '/var/lib/openshift/56bd9c5189f5cfeaba00009d/app-root/runtime/repo/wsgi/settings_production.py'
    exec(compile(open(file).read(), file, 'exec'))
    
# Heroku compatibility
import dj_database_url
if os.getcwd() == "/app":
    #db_from_env =  dj_database_url.config()
    #DATABASES['default'].update(db_from_env)
    
    
    DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.9/howto/static-files/
    '''
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
    STATIC_URL = '/static/'

    # Extra places for collectstatic to find static files.
    STATICFILES_DIRS = (
        os.path.join(PROJECT_ROOT, 'static'),
    )'''
