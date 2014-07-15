from django.contrib.gis.geos import *
from django.contrib.gis.measure import Distance, D

import difflib

# Full path to your django project directory
your_djangoproject_home="../"

import sys,os
sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hos2.settings'
 
from entries.models import ServiceProvider,Location,EffortInstance,ServiceType,EffortInstanceServices, Spatial_cluster_results, Similar_strings
 
#insert code to clear Deduplication tables
Similar_strings.objects.all().delete()
Spatial_cluster_results.objects.all().delete()

queryset = Location.objects.all()

#gets rid of the location points that don't have any geospatial data
queryset = Location.objects.exclude(point__isnull=True)

#print([p.point for p in queryset]) # Evaluate the query set.

print(queryset.count())

total_point_count = 0

total_point_sum = 0

for p in queryset:
	#print(p.point)
	pnt = p.point
	
	qs = Location.objects.filter(point__dwithin=(pnt,D(m=10)))
	
	#alternative query that does the same thing
	#qs = Location.objects.filter(point__distance_lt=(pnt,D(m=10)))
	
	#print(qs.count())
	
	if qs.count() > 5:
		#print(qs.count())
		Spatial_cluster_resultsObj = Spatial_cluster_results()
		
		Spatial_cluster_resultsObj.date_start = EffortInstance.objects.get(location=p.location_id).date_start
		
		Spatial_cluster_resultsObj.date_end = EffortInstance.objects.get(location=p.location_id).date_end
		
		Spatial_cluster_resultsObj.effort_instance_id = EffortInstance.objects.get(location=p.location_id).effort_instance_id
    
		Spatial_cluster_resultsObj.latitude = p.latitude
		Spatial_cluster_resultsObj.longitude = p.longitude
		
		Spatial_cluster_resultsObj.location_id = p.location_id
	
		provider_num = EffortInstance.objects.get(location=p.location_id).service_provider
		
		Spatial_cluster_resultsObj.service_provider = EffortInstance.objects.get(location=p.location_id).service_provider

		#print provider_num.provider
	
		Spatial_cluster_resultsObj.provider_name = ServiceProvider.objects.get(provider=provider_num.provider).provider_name
		
		Spatial_cluster_resultsObj.nearby_points = qs.count()
		
		Spatial_cluster_resultsObj.point_checked = False
	
		Spatial_cluster_resultsObj.save()
	
	total_point_count = total_point_count + 1

	total_point_sum = total_point_sum + qs.count()
	
print("total_point_count = ")
print(total_point_count)

print("total_point_sum = ")
print(total_point_sum)

queryset2 = Spatial_cluster_results.objects.all()

for a in queryset2:
	print("a point: ")
	print(a.point)

	pnt2 = a.point
	
	qs2 = Spatial_cluster_results.objects.filter(point__dwithin=(pnt2,D(m=10)))
	
	print('a location id: ')
	print(a.location_id)
	
	print('printing point_checked: ')
	print(Spatial_cluster_results.objects.get(location=a.location_id).point_checked)
	
	BoolMod = Spatial_cluster_results.objects.get(location=a.location_id)
	BoolMod.point_checked = True
	BoolMod.save()
	
	print('printing point_checked 2nd try: ')
	print(Spatial_cluster_results.objects.get(location=a.location_id).point_checked)
	
	#print(qs2)
	
	for b in qs2:
		print("b point: ")
		print(b.point)
		
		if Spatial_cluster_results.objects.get(location=b.location_id).point_checked == False:
		
			#compare similarities, need to add similarities to similar_strings table
			a_point_name = ServiceProvider.objects.get(provider=EffortInstance.objects.get(location=a.location_id).service_provider.provider).provider_name
			b_point_name = ServiceProvider.objects.get(provider=EffortInstance.objects.get(location=b.location_id).service_provider.provider).provider_name
			print(a_point_name)
			print(b_point_name)
		
			print("difflib ratio: ")
			print(difflib.SequenceMatcher(None, a_point_name, b_point_name).ratio())
		
			Similar_stringsObj = Similar_strings()
		
			#Similar_stringsObj.effort_instance_id = Deduplication_results.objects.get(location=a.location_id)
			Similar_stringsObj.effort_instance_id = Spatial_cluster_results.objects.get(location=a.location_id)
		
			Similar_stringsObj.related_string_id = EffortInstance.objects.get(location=b.location_id).effort_instance_id
			Similar_stringsObj.similarity_score = difflib.SequenceMatcher(None, a_point_name, b_point_name).ratio()

			Similar_stringsObj.save()
			
			
			