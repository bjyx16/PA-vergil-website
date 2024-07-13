from .settings import *
import os
# import dj_database_url

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] # vergil.azurewebsites.net
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] 

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'PORT': '1433',
        'NAME': os.environ['DB_NAME'],
        'HOST': os.environ['DB_SERVER'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
    }
}