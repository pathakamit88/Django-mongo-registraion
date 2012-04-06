from django.conf.urls.defaults import patterns, include, url
from views import Home

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
)