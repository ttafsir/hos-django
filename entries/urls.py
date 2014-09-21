from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import Location

from entries import views

'''
urlpatterns = patterns('',
    url(r'^$', GeoJSONLayerView.as_view(model=Unit), name='units-json')
    url(r'^nearby/$',TemplateView.as_view(template_name='units/nearby.html'),name='near-me'),
    url(r'^nearby/find/$', 'units.views.find_rocks', name='find-rocks'),    
)
'''



urlpatterns = patterns('',
    #url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^$', GeoJSONLayerView.as_view(model=Location), name='location-json'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<entries_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<entries_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^find/$', 'entries.views.find_facilities', name='find-facilities'),
)