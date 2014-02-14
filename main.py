import os
import sys

os.environ['DJANGO_SETTINGS_MODULE']='settings'

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import django.code.handlers.wsgi
application=django.core.handlers.wsgi.WSGIHandler()
