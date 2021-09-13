"""
Django settings for techfluenzer project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from crispy_forms.tests.test_settings import CRISPY_CLASS_CONVERTERS
from ckeditor_demo.settings import CKEDITOR_BROWSE_SHOW_DIRS, CUSTOM_TOOLBAR,\
    CKEDITOR_UPLOAD_PATH, CKEDITOR_ALLOW_NONIMAGE_FILES

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a2396cuijq%b68qv4)43szg$3joqa)l5a(=cim4n!w3)&lxf7t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


CRISPY_TEMPLATE_PACK = 'bootstrap4'

CRISPY_FAIL_SILENTLY = not DEBUG

CRISPY_CLASS_CONVERTERS = {'textinput': "textinput inputtext"}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'crispy_forms',
    'registration',
    'ckeditor',
    'ckeditor_uploader',
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'techfluenzer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processor.NewsletterSignUpFormGlobal',
                'blog.context_processor.CategoryGlobal',
                'blog.context_processor.RecentGlobal',
                'blog.context_processor.CategoryViewGlobal',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'techfluenzer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


ACCOUNT_ACTIVATION_DAYS=3       #mail will be active for 3 days
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS= True

EMAIL_HOST= 'smtp.gmail.com' #simple mail transfer protocol server            #when someone registers then it sends email to that person
EMAIL_HOST_USER= ''
EMAIL_HOST_PASSWORD= ''
EMAIL_PORT= 587



LOGIN_REDIRECT_URL = "/blog/home/"


PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
MEDIA_ROOT = PROJECT_ROOT + '/static/'
MEDIA_URL = '/media/'


from ckeditor.configs import DEFAULT_CONFIG

CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_UPLOAD_PATH = "blog/uploads/"
CKEDITOR_ALLOW_NONIMAGE_FILES = True





