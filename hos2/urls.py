from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.gis import admin

from entries import views as e_views

admin.autodiscover()

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',TemplateView.as_view(template_name='entries/main.html'),name='main'),
    url(r'^find/$', e_views.find_facilities, name='find-facilities'),
    url(r'^all/$', e_views.all_facilities, name='all-facilities'),
    url(r'^entries/', include('entries.urls', namespace='entries')),
]


#
