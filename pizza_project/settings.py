"""
Django settings for pizza_project project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(9_(p9t#+mx78=m22y5f&ru*(m8n35piz$n=7q*b-xm+9@k^_q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'channels',
    'notifications',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party apps for REST interface
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',

    # TASK QUEUES NEW
    'django_rq',

    #Our pizza apps
    'login_app',
    'pizza_app',


]

# Channels SETTINGS - NEW
ASGI_APPLICATION = 'pizza_project.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

## TASK QUEUES SETTINGS FOR EMAIL, MATCHES REDIS SERVER PORT ON LOCALHOST

RQ_QUEUES = {
    'default': {
    'HOST': 'localhost',
    'PORT': '6379',
    'DB': 0,
    'DEFAULT_TIMEOUT': 360,
    }
}

# EMAIL SETTINGS

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
#EMAIL_USE_SSL = True ### <--- DON'T USE THIS - USE EMAIL_USE_TLS
EMAIL_HOST = 'smtp.zoho.eu'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'joshua@ptd-cph.com'
EMAIL_HOST_PASSWORD = '9ywN15asjmZL'

# Setting up permissions and authorization settings for REST API
REST_FRAMEWORK = {
   'DEFAULT_PERMISSION_CLASSES': [
      # Use below if you want to make a custom permission class
      'pizza_app.permissions.IsEmployeeOrNoAccess',

      # Use below if you want to use Django default admin permissions
      'rest_framework.permissions.IsAdminUser'

      # Use below if you want to use token authentication.
      #'rest_framework.permissions.IsAuthenticated',
   ],
   'DEFAULT_AUTHENTICATION_CLASSES': [
      # Use below if you want to use token authentication.
      #'rest_framework.authentication.TokenAuthentication',
      
      # Use below if you want to use session authentication.
      'rest_framework.authentication.SessionAuthentication',
   ]
}

IPFILTER_MIDDLEWARE = {
    'ALLOWED_IP_ADDRESSES': [
        '127.0.0.1',
    ]
}

MIDDLEWARE = [
    'pizza_app.middleware.IPFilterMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pizza_project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'pizza_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
