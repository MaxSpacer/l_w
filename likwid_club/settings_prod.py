DEBUG = False
ALLOWED_HOSTS = ['46.101.118.243']

#settings for db on server
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'likwid_db1',
        'USER': 'django_likwid',
        'PASSWORD': 'Dl123456',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = '1025'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "info@likwid.club"
EMAIL_HOST_PASSWORD = "Il123456!"
EMAIL_USE_SSL = True
# SERVER_EMAIL = EMAIL_HOST_USER
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
