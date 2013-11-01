from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import main.urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('main.urls')),
)
