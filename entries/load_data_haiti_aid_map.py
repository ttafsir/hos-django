# Full path and name to your csv file

csv_filepathname="./data/20140413_Haiti_Aid_Map_utf8.csv"

# Full path to your django project directory

your_djangoproject_home="../"

import sys,os
sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hos2.settings'
 
from entries.models import ServiceProvider,Location,EffortInstance,ServiceType,EffortInstanceServices
 
import csv
#module used for regular expressions
import re
import random

#loads the classify_service_types dictionary, used to classify the service types
from service_type_dict import classify_service_types

print classify_service_types


dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
 
#The objects can't have the same name as the class, and a new object needs to be created each time a row is looped through

for row in dataReader:

	#print 'hi'
		
	if row[0] != 'id': # Ignore the header row, import everything else
	
		#checks to see if sector category is health
		if re.search('Health',row[12]):
		
			
			EffortInstanceObj = EffortInstance()
		
			EffortInstanceObj.effort_instance_id = row[0]
		

			 
			split = re.split(r'\/', row[9].strip())
		
			print split[2] + '-' + split[0] + '-' + split[1]
		
			EffortInstanceObj.date_start = split[2] + '-' + split[0] + '-' + split[1]
		
		
			split = re.split(r'\/', row[10].strip())
		
			print split[2] + '-' + split[0] + '-' + split[1]
		
			EffortInstanceObj.date_end = split[2] + '-' + split[0] + '-' + split[1]
		
		
			#cool way to make Service Providers unique, if obj does not exist then it creates it.
			#https://docs.djangoproject.com/en/1.6/ref/models/querysets/#get-or-create
			ServiceProviderObj, created = ServiceProvider.objects.get_or_create(provider_name = row[1])
		

		
			EffortInstanceObj.service_provider = ServiceProvider.objects.get(provider_name=row[1])
		

			loc = Location()
		
		
			loc.latitude = str(random.randint(0,10))
		
			loc.longitude = str(random.randint(0,10))
		
			loc.save()
		
	
			#need a way first in seeing if a location exists close by
			#EffortInstanceObj.location = loc.objects.get
			EffortInstanceObj.save()
		
		
			'''
			#looking at specialities column
			if row[3]:
				#print row[3]
			
			
				ServiceTypeSplit = re.split(r',', row[3].strip())
				#print ServiceTypeSplit
				for x in range(0,len(ServiceTypeSplit)):
				
				
					EffortInstanceServicesObj = EffortInstanceServices()
					EffortInstanceServicesObj.effort_instance = EffortInstance.objects.get(effort_instance_id=row[0])
				
					EffortInstanceServicesObj.effort_service_description = ServiceTypeSplit[x].strip()
				
				
					#classifies EffortInstanceServicesObj.effort_service_description based on a dictionary
					EffortInstanceServicesObj.effort_service_type = ServiceType.objects.get(service_name=classify_service_types[EffortInstanceServicesObj.effort_service_description])
				
					EffortInstanceServicesObj.save()	
			
			'''

	

