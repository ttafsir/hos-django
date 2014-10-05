# Full path and name to your csv file

csv_filepathname="./data/20140419_mmex_utf8.csv"

# Full path to your django project directory

your_djangoproject_home="../"

import sys,os
sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hos2.settings'
 
from entries.models import ServiceProvider,Location,EffortInstance,ServiceType,EffortInstanceService,haiti_adm1_minustah,haiti_adm3_minustah
 
import csv
#module used for regular expressions
import re
import random
import time
import datetime

ts = time.time()
utc_datetime = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

#loads the classify_service_types dictionary, used to classify the service types
from service_type_dict import classify_service_types

#loads the classify_adm1_names dictionary, used to classify the admin 1 boundaries
from adm1_name_dict import classify_adm1_names

#loads the classify_adm3_names dictionary, used to classify the admin 3 boundaries
from adm3_name_dict import classify_adm3_names

print classify_service_types

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
 
#The objects can't have the same name as the class, and a new object needs to be created each time a row is looped through

for row in dataReader:

	#print 'hi'
		
	if row[0] != 'id': # Ignore the header row, import everything else
		
		EffortInstanceObj = EffortInstance()
		
		EffortInstanceObj.effort_instance_id = row[0]
		
		if row[1] == 'Long-term':
			EffortInstanceObj.date_start = '9999-12-31'
			#print 'hey'
		else:
			#need to parse and re-enter the date format as year-month-day for django to like it'
			 
			split = re.split(r'\/', row[1].strip())
			
			print split[2] + '-' + split[0] + '-' + split[1]
			
			EffortInstanceObj.date_start = split[2] + '-' + split[0] + '-' + split[1]
		
		
		#ServiceProviderObj = ServiceProvider()
		
		#cool way to make Service Providers unique, if obj does not exist then it creates it.
		#https://docs.djangoproject.com/en/1.6/ref/models/querysets/#get-or-create
		ServiceProviderObj, created = ServiceProvider.objects.get_or_create(provider_name = row[2])
		
		#ServiceProviderObj.provider_name = row[2]
		
		#ServiceProviderObj.save()
		
		EffortInstanceObj.service_provider = ServiceProvider.objects.get(provider_name=row[2])
		
		EffortInstanceObj.updated_on = utc_datetime
		
		EffortInstanceObj.updated_by = 'MMEX scrape'
		
		#mmex does not have any lat lon coords, so don't add a location point
		#Also, don't use random lat lon. It will break spatial queries
	
		#loc = Location()
		#loc.latitude = str(random.randint(0,10))
		#loc.longitude = str(random.randint(0,10))
		#loc.save()
		
		
		'''
		Insert new code here to match admin boundaries: The location_information column is in column 11 (row [10]). This contains a list
		of admin boundaries where the facility is located at. The list contains entries with single quotes delimited with commas, and the list is 
		enveloped with brackets. The last entry on the list is Haiti. The second to last entry is an admin 1 boundary. The third to last entry
		is the admin 1 boundary.
		'''
		
		if row[10]:
			
			split_loc = row[10].replace("[", "")
			
			split_loc = split_loc.replace("]", "")
			
			split_loc = split_loc.replace("'", "")
			
			split_loc = split_loc.replace(" ", "")
			
			split_loc = re.split(r',', split_loc.strip())
			
			if len(split_loc) > 2:
			
				UpperAdmin1 = split_loc[len(split_loc) - 2].upper()
				
				print UpperAdmin1
				
				UpperAdmin2 = split_loc[len(split_loc) - 3].upper()
			
				print UpperAdmin2
				
				
				try:
				
					EffortInstanceObj.adm_1 = haiti_adm1_minustah.objects.get(adm1=classify_adm1_names[UpperAdmin1])
					
				except:
				
					print "guess no match"
				
				try:
					#https://docs.djangoproject.com/en/1.6/ref/models/querysets/#django.db.models.query.QuerySet
					#should retrieve the object where adm3 and adm1 match, this is needed because some admin 3 names are the same yet in different admin 1 areas
					EffortInstanceObj.adm_3 = haiti_adm3_minustah.objects.get(adm3=classify_adm3_names[UpperAdmin2],adm1=classify_adm1_names[UpperAdmin1])
					
				except:
				
					print "guess no match"
		
	
		#need a way first in seeing if a location exists close by
		#EffortInstanceObj.location = loc.objects.get
		EffortInstanceObj.save()
		
		#looking at specialities column
		if row[3]:
			#print row[3]
			
			
			ServiceTypeSplit = re.split(r',', row[3].strip())
			print ServiceTypeSplit
			for x in range(0,len(ServiceTypeSplit)):
				
				
				EffortInstanceServiceObj = EffortInstanceService()
				EffortInstanceServiceObj.effort_instance = EffortInstance.objects.get(effort_instance_id=row[0])
				
				EffortInstanceServiceObj.effort_service_description = ServiceTypeSplit[x].strip()
				
				print EffortInstanceServiceObj.effort_service_description
				
				#classify EffortInstanceServiceObj.effort_service_description based on a dictionary
				EffortInstanceServiceObj.effort_service_type = ServiceType.objects.get(service_name=classify_service_types[EffortInstanceServiceObj.effort_service_description])
				
				EffortInstanceServiceObj.save()	
			
		

	

