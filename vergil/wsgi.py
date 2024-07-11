"""
WSGI config for vergil project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

is_prod = 'WEBSITE_HOSTNAME' in os.environ
settings_module = 'vergil.production' if is_prod else 'vergil.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
