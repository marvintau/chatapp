import os

from django.core.wsgi import get_wsgi_application
import socketio

from .views import sio

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatserver.settings")

application = socketio.WSGIApp(sio, get_wsgi_application())