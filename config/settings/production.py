# Note about environment variables in Production
# Unlike Development, .env files do not work in production, that's the whole point of .env
# So set the ENV vars in the server

from .base import *
import dj_database_url
import os

SECRET_KEY = os.environ['SECRET_KEY']
DATABASE_URL = os.environ['DATABASE_URL']

db_from_env = dj_database_url.config(conn_max_age=500) # Why this?

DATABASES = {
    'default': dj_database_url.config(
        default = dj_database_url.config(DATABASE_URL)
    )
}

# Production Specific Middlewares
MIDDLEWARE = [
'whitenoise.middleware.WhiteNoiseMiddleware',
] + MIDDLEWARE

# Allow All hosts
ALLOWED_HOSTS = ['*']

# STATIC FILES
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = []

# Django does not allow you to serve static files from the same server in Production
# So using whitenoise is mandatory here.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
