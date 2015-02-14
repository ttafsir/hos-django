from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from djgeojson.views import GeoJSONLayerView
from .models import Location,EffortInstance

from entries import views


urlpatterns = patterns('',
    # ex: /entries/   It returns the Location table as a GeoJSON layer view
    url(r'^$', GeoJSONLayerView.as_view(model=Location), name='location-json'),
    url(r'^test_form/',TemplateView.as_view(template_name='entries/test_form.html'),name='test-form'),
    # ex: /entries/11795/results/   This returns the services that are provided by the specified Effort Instance
    # url(r'^(?P<pk>\d+)/results/$', DetailView.as_view(model=EffortInstance,template_name='entries/detail.html'), name='results'),
    #arg in views needs to be self and pk
    url(r'^(?P<pk>\d+)/results/$', views.service_results, name='service-results'),
    url(r'^shared_servicetype/$', 'entries.views.shared_servicetype', name='shared-servicetype'),
    # A post_request is called internally by the test_form to create a new organization
    url(r'^post_request/$', views.post_request, name='post-request'),
)

'''
There was an issue with the reverse call working for post-request
I tried with the url and with the name; it ended up working with the namespace
django shell:
In [30]: reverse('entries:post-request')
Out[30]: '/entries/post_request/'

>>> from django.core.urlresolvers import reverse
>>> reverse('entries:post-request')
'''