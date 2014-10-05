"""
Django settings for hos2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0w-_45z8rw!3o54!ei&%zt!f-xu7a8-)u$au1o25j3ui+%^-x&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# added django.contrib.gis for GeoDjango
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'djgeojson',
    'entries',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hos2.urls'

WSGI_APPLICATION = 'hos2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'postgres',
		'NAME': 'hos1',
		'PASSWORD': '',
		'HOST': 'localhost',
		'PORT': '5432',
    }
}

#GeoDjango version above

'''
{
    'default': {
		'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'hosadmin',
		'NAME': 'hos4',
		'PASSWORD': 'hosadmin',
		'HOST': 'hos4.c00fcyyjglve.us-east-1.rds.amazonaws.com',
		'PORT': '5432',
    }
}

{
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
		'NAME': 'hos1',
		'PASSWORD': 'HO$1',
		'HOST': 'hos-database.noip.me',
		'PORT': '5432',
    }
}
'''
'''
{
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'postgres',
		'NAME': 'hos1',
		'PASSWORD': '',
		'HOST': 'localhost',
		'PORT': '5432',
    }
}

{
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres',
		'NAME': 'django',
		'PASSWORD': '',
		'HOST': 'localhost',
		'PORT': '5432',
    }
}

'''



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

#changing to false because got a warning of received a naive datetime while time zone support is active.
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
