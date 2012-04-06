from django.conf.urls.defaults import patterns, include, url
from mongo_login.views import register

urlpatterns = patterns('',
    url(r'^register/$', register, name='register'),
)