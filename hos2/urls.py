from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
from django.contrib.gis import admin

from entries import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hos2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',TemplateView.as_view(template_name='entries/main.html'),name='main'),
    url(r'^find/$', 'entries.views.find_facilities', name='find-facilities'),
    url(r'^all/$', 'entries.views.all_facilities', name='all-facilities'),
    url(r'^entries/', include('entries.urls', namespace='entries',app_name='entries')),
    url(r'^admin/', include(admin.site.urls)),
)
