from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^$', main),
    url(r'^send/', save),
)
