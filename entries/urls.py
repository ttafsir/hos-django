from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse

from . import views
from .models import Location,EffortInstance

urlpatterns = [

    url(r'^$', views.GeoJSONView.as_view(), name='location-json'),
    url(r'^index/', views.IndexView.as_view(), name="index"),
    url(r'^test_form/', views.FormView.as_view(), name="test_form"),
    url(r'^(?P<pk>\d+)/results/$', views.service_results, name='service-results'),
    url(r'^shared_servicetype/$', views.shared_servicetype, name='shared-servicetype'),
    url(r'^post_request/$', views.post_request, name='post-request'),
]


'''
There was an issue with the reverse call working for post-request
I tried with the url and with the name; it ended up working with the namespace
django shell:
In [30]: reverse('entries:post-request')
Out[30]: '/entries/post_request/'

>>> from django.core.urlresolvers import reverse
>>> reverse('entries:post-request')
'''
