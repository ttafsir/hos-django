from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.gis.geos import Point
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.contrib.gis.geos import *
from django.contrib.gis.measure import Distance, D

from entries.models import EffortInstance,EffortInstanceServices,Location

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'entries/index.html'
	context_object_name = 'latest_EffortInstance_list'
	
	def get_queryset(self):
		"""Return the last five published EffortInstances."""
		return EffortInstance.objects.order_by('-date_start')[:15]
 
#example using a generic DetailView
#notice that there is no 'entry' being passed, the effortinstance variable is being provided automatically using the Django model
class DetailView(generic.DetailView):
	model = EffortInstance
	template_name = 'entries/detail.html'
	       
'''  
#This is the previous example  
def detail(request, entries_id):
    entry = get_object_or_404(EffortInstance, effort_instance_id=entries_id)
    #This 'entry' object, which is an EffortInstance object gets passed along to the detail template
    return render(request, 'entries/detail.html', {'entry': entry})
'''
    
def results(request, entries_id):
    entry = get_object_or_404(EffortInstance, effort_instance_id=entries_id)
    return render(request, 'entries/results.html', {'entry': entry})

'''
def vote(request, entries_id):
    entry = get_object_or_404(EffortInstance, effort_instance_id=entries_id)
    try:
        selected_choice = entry.effortinstanceservices_set.get(effort_instance_service_id=request.POST['service'])
    except (KeyError, EffortInstanceServices.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'entries/detail.html', {
            'entry': entry,
            'error_message': "You didn't select a service.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('entries:results', args=(p.id,)))
'''
        
def find_facilities(request):

	"""
	Give a lat/lon pair, return the unit(s) surround it.
	"""
	#example of a get request: http://127.0.0.1:8000/find/?lat=38.8826044&lon=-77.105
	#example of a get request: http://127.0.0.1:8000/find/?lat=18.57&lon=-72.292

	
	#if request.is_ajax():
	lat = request.GET.get('lat', None)
	lon = request.GET.get('lon', None)
	
	#need a buffer distance...
  
        
    #else: 
    	#msg = "Bad request: no AJAX present"
    	#return HttpResponseBadRequest(msg)
        
	#point = Point(float(lon), float(lat))
	lon = float(lon)
	lat = float(lat)
	point2 = Point(lon,lat)
	#point2 = Point(lat,lon)
	
	#return HttpResponse(lon)
	
	
	pnt = Point(-104.93, 39.73)
	
	#units = Unit.objects.filter(geom__contains=point2)
	#facilities = Location.objects.filter(geom__contains=point2)
	#facilities = Location.objects.filter(geom__contains=point2)
	#facilities = Location.objects.filter(point__dwithin=(point2, D(m=5000)))
	facilities = Location.objects.filter(geom__distance_lt=(point2, D(m=100)))
	#geojson_data = GeoJSONSerializer().serialize(Unit.objects.all(), use_natural_keys=True) 
	
	print ('hello')
	
	#originally I tried .get() , but that returned a MultipleObjectsReturned error
	#so I changed it to .filter()
	#results = Unit.objects.filter(name="Intrusion")
	
	
	geojson_data = GeoJSONSerializer().serialize(facilities, use_natural_keys=True) 
	
	'''
	if lat and lon:
		#foo2 = "Hello, world. You're at %s." % lat
		foo3 = facilities
		return HttpResponse(foo3)
		#return HttpResponse("Hello, world. You're at nowhere.")
	'''
	
	#return HttpResponse(geojson_data,content_type='application/json')
	
	#else:   
		#msg = "Bad request: no latlong pair present"
		#return HttpResponseBadRequest(msg)
