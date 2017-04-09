from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^artigo/(?P<artigo_id>\d+)/$', views.artigo, name='artigo'),
]
