# Full path and name to your csv file

#csv_filepathname="/Users/thomasgertin1/hos-django/entries/20140415_HAC_utf8.csv"
csv_filepathname="./data/20140419_mmex_utf8.csv"

# Full path to your django project directory

#your_djangoproject_home="/Users/thomasgertin1/hos-django/"
# two directories up. Chained!
#your_djangoproject_home="../../hos-django/"
your_djangoproject_home="../"

import sys,os
sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hos2.settings'
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hos2.settings")
 
from entries.models import ServiceProvider,Location,EffortInstance,ServiceType,EffortInstanceServices
 
import csv

#module used for regular expressions
import re

import random

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
 
#ServiceType = ServiceType()

EffortInstance = EffortInstance()

Location = Location()

ServiceProvider = ServiceProvider()

#EffortInstanceServices = EffortInstanceServices()

EffortInstanceCount = 1

for row in dataReader:

	print 'hi'
	
		
	if row[0] != 'id': # Ignore the header row, import everything else
		
		
		#Location.location_id = row[0]
		
		#will need to autoincrement id in code maybe?
		
		Location.latitude = random.randint(0,10)
		
		#Location.longitude = random.randint(0,10)
		
		
		Location.save()
		
		print 'location'
		
		EffortInstance.effort_instance_id = row[0]
		
		ServiceProvider.provider_name = row[2]
		
		ServiceProvider.save()
		
		if row[1] == 'Long-term':
			EffortInstance.date_start = '9999-12-31'
			print 'hey'
		else:
			#need to parse and re-enter the date format as year-month-day for django to like it'
			 
			split = re.split(r'\/', row[1].strip())
			
			print split[2] + '-' + split[0] + '-' + split[1]
			
			EffortInstance.date_start = split[2] + '-' + split[0] + '-' + split[1]
		
		
		#EffortInstance.save()
		
		ObjDict = {}
		
		#looking at specialities column
		if row[3]:
			#print row[3]
			ServiceTypeSplit = re.split(r',', row[3].strip())
			print ServiceTypeSplit
			for x in range(0,len(ServiceTypeSplit)):
				
				ObjDict[EffortInstanceCount] = EffortInstanceServices(effort_instance_service_id = EffortInstanceCount, effort_instance = EffortInstance)
				#EffortInstanceServices.effort_instance_service_id = EffortInstanceCount
				#EffortInstanceServices.effort_instance = EffortInstance
				EffortInstanceCount = EffortInstanceCount + 1
				
				ObjDict[EffortInstanceCount].save()
				
				
		EffortInstance.save()
		
		
	
	print 'bye'
	

