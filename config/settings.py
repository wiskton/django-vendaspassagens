# coding: utf-8
import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Willem', 'willemarf@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# -------------------------------------------------------------
# LOCALE 
# -------------------------------------------------------------

TIME_ZONE = 'America/Sao_Paulo'

# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

USE_I18N = True
USE_L10N = True
USE_TZ = False

gettext = lambda s: s
LANGUAGES = (
    ('pt', gettext(u'Português')),
    ('en', gettext(u'Inglês')),
    ('es', gettext('Espanhol')),
)

LOCALE_PATHS = (
    os.path.join( PROJECT_PATH, '../locale' ),
)

SITE_ID = 1


# -------------------------------------------------------------
# PROJETO 
# -------------------------------------------------------------

MEDIA_ROOT = os.path.join(PROJECT_PATH, '..', 'media')
MEDIA_URL = '/media/'


STATIC_ROOT = os.path.join(PROJECT_PATH, '..', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # os.path.join(PROJECT_PATH, '..', 'static'),
    os.path.join(PROJECT_PATH, '..', 'public'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, '..', 'templates')
)

ROOT_URLCONF = 'config.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'config.wsgi.application'


# -------------------------------------------------------------
# INSTALLED_APPS 
# -------------------------------------------------------------

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'consulta',

    # 'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.sites',
    # 'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    #'south',
)


# -------------------------------------------------------------
# EMAIL 
# -------------------------------------------------------------

EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT="587"
EMAIL_HOST_USER="contato@willemallan.com.br"
EMAIL_HOST_PASSWORD="a1b2c3d4"
EMAIL_USE_TLS=True


# -------------------------------------------------------------
# OUTROS 
# -------------------------------------------------------------

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'dm*wh*et4k()b#s^7&amp;)ews#6&amp;wzxd$0+qy8$7k)ham!6p%hqee'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    # 'app.middleware_i18n.ForceDefaultLanguageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# -------------------------------------------------------------
# LOGGING
# -------------------------------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# -------------------------------------------------------------
# SETTINGS 
# -------------------------------------------------------------
try:
    from local_settings import *
except ImportError:
    print 'local_settings.py not found'