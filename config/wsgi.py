import os
from django.core.wsgi import get_wsgi_application

settings_module = 'config.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'config.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
