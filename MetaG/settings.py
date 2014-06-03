"""
Django settings for MetaG project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECRET_KEY should be set using environment variable in production!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
        '.ee.',
        ]

SESSION_COOKIE_SECURE = True

ADMINS = (
        ('MetaG admin', 'metag@moonfish.ttu.ee'),
        )

# Application definition

INSTALLED_APPS = (
    'fileupload',
    'jquery',
    'Umanager',
    'Pmanager',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'MetaG.urls'

WSGI_APPLICATION = 'MetaG.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
            os.path.join(BASE_DIR, "static"),
# For use with apache at deployment
#                '/var/www/MetaG/static/',
                )

# Send to Umanager's login view every time @login_required view is
# accessed without authorisation.

LOGIN_URL='/user/login'

# resumable upload specific settings
# !!! Check if we still want to preserve these

# FILE_UPLOAD_MAX_MEMORY_SIZE=262144
# FILE_UPLOAD_TEMP_DIR=os.path.join(BASE_DIR, 'files/tmp')

# Defined for 'fileupload' - we might change these soon

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, "media")

# When 'DEV_METAG' is set in ~/.bashrc , override some settings with
# settings_dev.py as well as add some debuging and other useful stuff
# for development. Naturally, settings_dev.py is excluded from repository
# commit.

if os.environ.get('DEV_METAG', None):
    try:
        from MetaG.settings_dev import *
    except ImportError:
        pass
