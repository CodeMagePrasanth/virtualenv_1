"""
ASGI config for project36_detailView_Dynamic_Url_mapping project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project36_detailView_Dynamic_Url_mapping.settings')

application = get_asgi_application()
