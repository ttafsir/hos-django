from django.contrib.gis.geos import *
from django.contrib.gis.measure import Distance, D

import difflib

# Full path to your django project directory
your_djangoproject_home="../"

import sys,os
sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hos2.settings'
 
from entries.models import ServiceProvider,Location,EffortInstance,ServiceType,EffortInstanceServices,Spatial_cluster_results,Admin_cluster_results,Similar_strings,haiti_adm3_minustah
 
#insert code to clear Deduplication tables
Similar_strings.objects.all().delete()
Spatial_cluster_results.objects.all().delete()
Admin_cluster_results.objects.all().delete()


def SimilarityQuery (inputquery, querytype):

	if querytype == 'admin_query':
		Admin_cluster_results.objects.all().delete()
		for d in inputquery:
		
			#write the temporary points in admin3 table
			Admin_cluster_resultsObj = Admin_cluster_results()
			Admin_cluster_resultsObj.date_start = EffortInstance.objects.get(location=d.location_id).date_start
			Admin_cluster_resultsObj.date_end = EffortInstance.objects.get(location=d.location_id).date_end
			Admin_cluster_resultsObj.effort_instance_id = EffortInstance.objects.get(location=d.location_id).effort_instance_id
			Admin_cluster_resultsObj.latitude = d.latitude
			Admin_cluster_resultsObj.longitude = d.longitude
			Admin_cluster_resultsObj.location_id = d.location_id
			provider_num = EffortInstance.objects.get(location=d.location_id).service_provider
			Admin_cluster_resultsObj.service_provider = EffortInstance.objects.get(location=d.location_id).service_provider
			Admin_cluster_resultsObj.provider_name = ServiceProvider.objects.get(provider=provider_num.provider).provider_name
			Admin_cluster_resultsObj.nearby_points = qs.count()
			Admin_cluster_resultsObj.point_checked = False
			Admin_cluster_resultsObj.save()
		
	for a in inputquery:
		print("a point: ")
		print(a.point)

		pnt2 = a.point
	
		if querytype == 'proximity_query':
		
			qs2 = Spatial_cluster_results.objects.filter(point__dwithin=(pnt2,D(m=10)))
			
		if querytype == 'admin_query':
		
			print('must be admin_query')
			qs2 = inputquery
			
	
		print('a location id: ')
		print(a.location_id)
	
		if querytype == 'proximity_query':
		
			print('printing point_checked: ')
			print(Spatial_cluster_results.objects.get(location=a.location_id).point_checked)
	
			#Mark the point that is checking it's neighbors True, so it's neighbors won't recheck it
			BoolMod = Spatial_cluster_results.objects.get(location=a.location_id)
			BoolMod.point_checked = True
			BoolMod.save()
	
			print('printing point_checked 2nd try: ')
			print(Spatial_cluster_results.objects.get(location=a.location_id).point_checked)
			
		if querytype == 'admin_query':
		
			#Mark the point that is checking it's neighbors True, so it's neighbors won't recheck it
			BoolMod = Admin_cluster_results.objects.get(location=a.location_id)
			BoolMod.point_checked = True
			BoolMod.save()
	
			#print(qs2)
	
		for b in qs2:
			print("b point: ")
			print(b.point)
	
			if querytype == 'proximity_query':
				if Spatial_cluster_results.objects.get(location=b.location_id).point_checked == False:
	
					#compare similarities, need to add similarities to similar_strings table
					a_point_name = ServiceProvider.objects.get(provider=EffortInstance.objects.get(location=a.location_id).service_provider.provider).provider_name
					b_point_name = ServiceProvider.objects.get(provider=EffortInstance.objects.get(location=b.location_id).service_provider.provider).provider_name
				
					print(a_point_name)
					print(b_point_name)

					print("difflib ratio: ")
					print(difflib.SequenceMatcher(None, a_point_name, b_point_name).ratio())
					
					if difflib.SequenceMatcher(None, a_point_name, b_point_name).ratio() > .5:
					
						#The following three lines are supposed to only display IDs that come from different datasets
						id_one = Spatial_cluster_results.objects.get(location=a.location_id).effort_instance_id
						id_two = EffortInstance.objects.get(location=b.location_id).effort_instance_id
						if not str(id_one)[0] == str(id_two)[0]:

							Similar_stringsObj = Similar_strings()

							#if querytype == 'proximity_query':
							#Similar_stringsObj.effort_instance_id = Spatial_cluster_results.objects.get(location=a.location_id)
							Similar_stringsObj.string_id = Spatial_cluster_results.objects.get(location=a.location_id).effort_instance_id

							Similar_stringsObj.related_string_id = EffortInstance.objects.get(location=b.location_id).effort_instance_id
							Similar_stringsObj.similarity_score = difflib.SequenceMatcher(None, a_point_name, b_point_name).ratio()
							Similar_stringsObj.provider_name = a_point_name
							Similar_stringsObj.related_provider_name = b_point_name
							Similar_stringsObj.save()
			
			if querytype == 'admin_query':
				if Admin_cluster_results.objects.get(location=b.location_id).point_checked == False:
	
					#compare similarities, need to add similarities to similar_strings table
					a_point_name = ServiceProvider.objects.get(provider=EffortInstance.objects.get(location=a.location_id).service_provider.provider).provider_name
					b_point_name = ServiceProvider.objects.get(provider=EffortInstance.objects.get(location=b.location_id).service_provider.provider).provider_name
					
					print(a_point_name)
					print(b_point_name)

					print("difflib ratio: ")
					print(difflib.SequenceMatcher(None, a_point_name, b_point_name).ratio())
					
					if difflib.SequenceMatcher(None, a_point_name, b_point_name).ratio() > .1:

						#The following three lines are supposed to only display IDs that come from different datasets
						id_one = Spatial_cluster_results.objects.get(location=a.location_id).effort_instance_id
						id_two = EffortInstance.objects.get(location=b.location_id).effort_instance_id
						if not str(id_one)[0] == str(id_two)[0]:

							Similar_stringsObj = Similar_strings()

							#if querytype == 'proximity_query':
							#Similar_stringsObj.effort_instance_id = Spatial_cluster_results.objects.get(location=a.location_id)
							Similar_stringsObj.string_id = Spatial_cluster_results.objects.get(location=a.location_id).effort_instance_id

							Similar_stringsObj.related_string_id = EffortInstance.objects.get(location=b.location_id).effort_instance_id
							Similar_stringsObj.similarity_score = difflib.SequenceMatcher(None, a_point_name, b_point_name).ratio()
							Similar_stringsObj.provider_name = a_point_name
							Similar_stringsObj.related_provider_name = b_point_name
							Similar_stringsObj.save()

queryset = Location.objects.all()

#gets rid of the location points that don't have any geospatial data
queryset = Location.objects.exclude(point__isnull=True)

#print([p.point for p in queryset]) # Evaluate the query set.

print(queryset.count())

total_point_count = 0

total_point_sum = 0

#loops through each point that has a geom
for p in queryset:
	#print(p.point)
	pnt = p.point
	
	#doesn't work when I changed the points to geometries from geography types
	#qs = Location.objects.filter(point__dwithin=(pnt,D(m=10)))
	
	#alternative query that does the same thing
	qs = Location.objects.filter(point__distance_lt=(pnt,D(km=20)))
	
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


#finding all of the admin3 boundaries
EffortInstance_queryset = EffortInstance.objects.all()

mylist = []

for b in EffortInstance_queryset:

	if b.adm_3:
		print(b.adm_3)
		mylist.append(b.adm_3)
		
myset = set(mylist)

print('printing output: ')
print myset

#need to compare to all points within the admin 3 polygon
#looping through all of the unique admin3 polygons
for c in myset:
	print(c)

	poly = c.geom
	
	#spatial query finds all points within each individual polygon
	point_qs = Location.objects.filter(point__within=poly)
	
	print(point_qs)
	#print(point_qs)
	print(len(point_qs))
	
	#initially turning off the admin SimilarityQuery
	#if len(point_qs) > 1:
		#SimilarityQuery(point_qs, 'admin_query')
		
			
SimilarityQuery(queryset2, 'proximity_query')
			
			