from django.urls import path, include
from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
]

from django.views.static import serve
from django.conf import settings

if not settings.DEBUG:
    urlpatterns += [url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})]