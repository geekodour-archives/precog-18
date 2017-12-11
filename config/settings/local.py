from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += ['debug_toolbar', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR/'db.sqlite3'),
    }
}

# Try adding toolbar to the top
MIDDLEWARE = [
'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

INTERNAL_IPS = '127.0.0.1'
STATIC_ROOT = BASE_DIR / 'static_root'
