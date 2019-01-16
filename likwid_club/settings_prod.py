DEBUG = False
ALLOWED_HOSTS = ['*']

#settings for db on server
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lwdb',
        'USER': 'likwid_root',
        'PASSWORD': 'Zz123456!',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}
