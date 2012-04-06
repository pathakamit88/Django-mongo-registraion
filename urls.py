from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from mongo_login.views import register

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^', include('dashboard.urls')),
    url(r'^', include('mongo_login.urls')),
    url(r'^account/', include('django.contrib.auth.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
