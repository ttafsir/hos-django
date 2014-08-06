from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.gis import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hos2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^entries/', include('entries.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
