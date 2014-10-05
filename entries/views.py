from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.gis.geos import Point
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.contrib.gis.geos import *
from django.contrib.gis.measure import Distance, D
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
from django.core import serializers

from entries.models import *

import difflib

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'entries/index.html'
	context_object_name = 'latest_EffortInstance_list'
	
	def get_queryset(self):
		"""Return the last five published EffortInstances."""
		return EffortInstance.objects.order_by('-date_start')[:15]
    
def results(request, entries_id):
    entry = get_object_or_404(EffortInstance, effort_instance_id=entries_id)
    return render(request, 'entries/results.html', {'entry': entry})


#disables csrf token validation on this view
@csrf_exempt
def post_request(request):
	
	organization = request.POST.get('organization', None)
	
	#this validation is not returning the HttpResponse for some reason...
	if len(organization) < 1:
		print('if org name is blank')
		return HttpResponse('Please fill in an Organization name')
	
	lat_str = request.POST.get('lat', None)
	lon_str = request.POST.get('lon', None)
	
	#make them only 15 characters
	lat_str = lat_str[:15]
	lon_str = lon_str[:15]
	
	lat = float(lat_str)
	lon = float(lon_str)
	
	input_point = Point(lon,lat)
	
	print('org name: ')
	print(organization)
	
	health_facilities_within_100_meters = Location_w_efforts.objects.filter(geom__distance_lt=(input_point, D(m=8000)))
	
	#Need to do something about Location_w_efforts table...
	#Need to do updates to HOS DB
	
	#tests to see if there is an existing organization name that is exactly the same
	try:
		#I needed to do a filter with starts_with for some reason, the good thing anyways is that 
		#it will catch multiple organizations if they all start with the same name
		selected_choice = Location_w_efforts.objects.filter(provider_name__startswith=organization)
		print(selected_choice)
		print(len(selected_choice))
		if len(selected_choice)<1:
			print("no matching org name, but a similar result")
			similar_name_list = []
			for i in Location_w_efforts.objects.all():
				#print(difflib.SequenceMatcher(None, organization, i.provider_name).ratio())
				if difflib.SequenceMatcher(None, organization, i.provider_name).ratio() > .95:
					similar_name_list.append(i.provider_name)
	except:
		print("exception")
	else:
		matching_facilities = GeoJSONSerializer().serialize(selected_choice, use_natural_keys=True)
		matching_facilities_list = simplejson.loads(matching_facilities)
	
	#tests to see if there are existing organization close by
	if health_facilities_within_100_meters > 0:
		nearby_facilities = GeoJSONSerializer().serialize(health_facilities_within_100_meters, use_natural_keys=True) 
		#print(nearby_facilities)
		nearby_facilities_list = simplejson.loads( nearby_facilities )
	else:
		nearby_facilities_list= ""
		
	print('json_data_input_list up next')
		
	json_data_input_list= {}
	
	if selected_choice:
		json_data_input_list['matching_facilities'] = matching_facilities_list
		print('matching fac')
	
	if nearby_facilities_list:
		print('matching fac 3')
		json_data_input_list['nearby_facilities'] = nearby_facilities_list
		print('matching fac 5')
		
	try:
		if len(similar_name_list) > 0:
			print('matching fac 4')
			similar_name_list = simplejson.loads(similar_name_list)
			json_data_input_list['similar_names'] = similar_name_list
	except NameError:
  		print("well, it WASN'T defined after all!")
	else:
	  	print("sure, it was defined.")
	
	
	print("ready to dump")
	
	json_data = simplejson.dumps(json_data_input_list)
	
	print(json_data)
	
	#helpful link: http://kiaran.net/post/54943617485/serialize-multiple-lists-of-django-models-to-json
	#json_data = simplejson.dumps( {'nearby_facilities':nearby_facilities_list, 'matching_facilities':matching_facilities_list})
	
	if json_data:
		print('returning')
		return HttpResponse(json_data,content_type='application/json')
	# if no nearby entry or entry with matching or similar name, then create a new entry
	else:
    	
		#before I used AJAX...
		#return HttpResponseRedirect('/entries/test_form/')
	
		#if it is a new organization name and in a new location then create new entry in DB
	
		#detects all of the services provided that were selected and puts in in a list
		service_list = []
	
		for e in ServiceType.objects.all():
			if (request.POST.get(e.service_name)):
				service_list.append(e.service_name)

   
		'''
		We want to append 55 to imported HOS site data
		find all IDs with 55 to the left, then find the max number,
		then separate the 55 and what is to the right, then find the next incremental value, then append
		'''
		the_55s = EffortInstance.objects.filter(effort_instance_id__startswith=111588)
		list_of_55s = []
		for i in the_55s:
			list_of_55s.append(i.effort_instance_id)
		highest_55 = max(list_of_55s)
		left_two = str(highest_55)[:2]
		to_the_right = str(highest_55)[2:]
		increment_one = int(to_the_right) + 1
		new_id = left_two + str(increment_one)
	
		EffortInstanceObj = EffortInstance()
		EffortInstanceObj.effort_instance_id = new_id
	
		#Create ServiceProvider
		ServiceProviderObj, created = ServiceProvider.objects.get_or_create(provider_name=organization)
		EffortInstanceObj.service_provider = ServiceProvider.objects.get(provider_name=organization)
	
		#insert default date for effortInstance

		#Create Location
		loc = Location()
		loc.latitude = lat_str
		loc.longitude = lon_str
		loc.save()
		EffortInstanceObj.location = Location.objects.get(id=loc.id)
		EffortInstanceObj.save()
	
		if loc.geom:
			qs = haiti_adm3_minustah.objects.filter(geom__contains=loc.geom)
			#return HttpResponse(qs[0])
		
			if len(qs):
			
				#return HttpResponse(qs[0].adm3)
				EffortInstanceObj.adm_3 = haiti_adm3_minustah.objects.get(id=qs[0].id)
				
			EffortInstanceObj.save()
	
	
		#Create Services
		for x in service_list:
				EffortInstanceServicesObj = EffortInstanceServices()
				EffortInstanceServicesObj.effort_instance = EffortInstance.objects.get(effort_instance_id=new_id)
	
				EffortInstanceServicesObj.effort_service_description = x
				
				EffortInstanceServicesObj.effort_service_type = ServiceType.objects.get(service_name=x)
	
				EffortInstanceServicesObj.save()
	
	
		#just consider a simple password for drupal to pass with each post for authentication
		#next step would be https
	
     
def find_facilities(request):

	"""
	Give a lat/lon pair, return the unit(s) surround it.
	"""
	#example of a get request: http://127.0.0.1:8000/find/?lat=18.57&lon=-72.293&buffer=1000
	
	#if request.is_ajax():
	lat = request.GET.get('lat', None)
	lon = request.GET.get('lon', None)
	
	#need a buffer distance...
  	buffer = request.GET.get('buffer', None)
  	
  	#make default buffer value 1000 if it is not specified
  	if not buffer:
  		buffer = 1000
        
    #else: 
    	#msg = "Bad request: no AJAX present"
    	#return HttpResponseBadRequest(msg)
        
	#point = Point(float(lon), float(lat))
	lon = float(lon)
	lat = float(lat)
	point2 = Point(lon,lat)
	
	#test_pnt = Point(-104.93, 39.73)
	

	"""
	Why distance_lt instead of dwithin?
	http://stackoverflow.com/questions/2235043/geodjango-difference-between-dwithin-and-distance-lt
	"""
	facilities = Location_w_efforts.objects.filter(geom__distance_lt=(point2, D(m=buffer)))
	
	'''
	originally I tried .get() , but that returned a MultipleObjectsReturned error
	so I changed it to .filter()
	If there will be more than one result, you need .filter()
	'''

	geojson_data = GeoJSONSerializer().serialize(facilities, use_natural_keys=True) 
	
	return HttpResponse(geojson_data,content_type='application/json')

def shared_servicetype(request):

	#example of a get request: http://127.0.0.1:8000/entries/shared_servicetype/?id=11779
	#11779 should have 7 services
	
	effort_instance_id = request.GET.get('id', None)
	
	print("ok")
	
	if effort_instance_id:
		
		try:
			selected_effort_instance = EffortInstance.objects.get(effort_instance_id=effort_instance_id)
			#related_effort_instances = EffortInstance.objects.filter(__in=selected_effort_instance.effortinstanceservices_set.all)
			
			#http://thebuild.com/blog/2010/12/22/getting-the-id-of-related-objects-in-django/
			#https://docs.djangoproject.com/en/1.6/topics/db/aggregation/
			#The .values is grabbing the unique service names for the selected effort instance
			all_services_qs = selected_effort_instance.effortinstanceservices_set.all().values('effort_service_type__service_name')
			
			#Python also includes a data type for sets. A set is an unordered collection with no duplicate elements.
			all_services = set([entry['effort_service_type__service_name'] for entry in all_services_qs])
			
			print('printing all services:')
			print(all_services)
			
			#The query chain below didn't work because you can't chain a _set.all() after a filter. You can I think after a get
			#ServiceType.objects.filter(service_name__in=['Pharmacy','Malaria']).effortinstanceservices_set.all().values('effort_instance_id')
			
			'''
			Tests that worked:
			print("all Service type objects with 2 picked:")
			print(ServiceType.objects.filter(service_name__in=['Pharmacy','Malaria']))
			
			print("all Service type objects with list picked:")
			print(ServiceType.objects.filter(service_name__in=all_services))
			'''
			
			#http://stackoverflow.com/questions/853184/django-orm-selecting-related-set
			sel_service_types = ServiceType.objects.filter(service_name__in=all_services)
			
			#You want distinct because many EffortInstanceServices objects will link to the same EffortInstance object, so you
			#don't want duplicates of EffortInstance objects selected
			sel_ids = EffortInstanceServices.objects.filter(effort_service_type__in=sel_service_types).values('effort_instance_id').distinct()
			
			print("Effort Instances that share at least one service type:")
			print(sel_ids)
		
		except:
			print("exception")
		else:
			print("else")
			return HttpResponse(sel_ids,content_type='application/json')
		
def all_facilities(request):

	"""
	returns all facilities from temp table
	"""
	
	"""
	Why am I using Location_w_efforts? 
	The serializer failed with Location, there might be a bug with the django-geojson plugin
	It is not handling backwards relations
	http://stackoverflow.com/questions/22898547/error-with-geodjango-serializer-and-foreignkey-field
	"""
	
	facilities = Location_w_efforts.objects.all()
	
	print ('hello')
		
	
	geojson_data = GeoJSONSerializer().serialize(facilities, use_natural_keys=True) 
	
	return HttpResponse(geojson_data,content_type='application/json')
	
	