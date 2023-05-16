from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    'obrasnet.views',
    url(r'^requirements', 'requirements', name='requirements')
)