DEBUG = False
ALLOWED_HOSTS = ['46.101.118.243']

#settings for db on server
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'likwid_db',
        'USER': 'django_likwid',
        'PASSWORD': 'Dl123456',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}
