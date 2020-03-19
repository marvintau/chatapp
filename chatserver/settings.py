import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

SECRET_KEY = '3ctkuns=obqwkcafs^vhl6iwn1#x01#s__&2gu*apr7b08(3=9'
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '120.77.243.97'
]

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'chatserver.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [],
        },
    },
]

WSGI_APPLICATION = 'chatserver.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../client", 'build')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static') 
