# Full path and name to your csv file
csv_filepathname="./data/20140415_HAC_utf8.csv"

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

hacHeaders = ["id","title","address ","arv","cardiovascular","dental","department ","diabetes","emergency","free_obstetric_care_program","general_consultation","hypertension","institution_code","intensive_care","laboratory","latitude ","longitude","malaria","number_of_adult_beds","number_of_pediatric_beds","obgyn","operating_room","orl ","palliative_care","pediatrics","pharmacy","physical_therapy","psychology_service","section","status","surgery","telephone","town ","type","vaccination"]

hacServiceCols = [3,4,5,7,8,9,10,11,13,14,17,20,21,22,23,24,25,26,27,30,34];

def upfirstletter(value):
    first = value[0] if len(value) > 0 else ''
    remaining = value[1:] if len(value) > 1 else ''
    return first.upper() + remaining
	
for row in dataReader:

	#print 'hi'
	
	if row[0] != 'id': # Ignore the header row, import everything else
		
		EffortInstanceObj = EffortInstance()
		
		EffortInstanceObj.effort_instance_id = row[0]
		if row[33] == 'Hopital' or row[33] == 'CSL' or row[33] == 'CAL':
			#EffortInstanceObj.date_start = '9999-12-31'
			print 'long-term recorded'
			
		if row[33] == 'Hopital':
			EffortInstanceObj.provider_type = 'HL'
			print 'hospital recorded'
		elif row[33] == 'CSL' or row[33] == 'CAL':
			EffortInstanceObj.provider_type = 'CL'
			print 'clinic recorded'
		
		#ServiceProviderObj = ServiceProvider()
		
		#cool way to make Service Providers unique, if obj does not exist then it creates it.
		#https://docs.djangoproject.com/en/1.6/ref/models/querysets/#get-or-create
		ServiceProviderObj, created = ServiceProvider.objects.get_or_create(provider_name = row[1])
		
		EffortInstanceObj.service_provider = ServiceProvider.objects.get(provider_name=row[1])
		EffortInstanceObj.save()
		
		
		for x in range(0,len(hacServiceCols)):
			if hacServiceCols[x] == "1":
				EffortInstanceServicesObj = EffortInstanceServices()
				EffortInstanceServicesObj.effort_instance = EffortInstance.objects.get(effort_instance_id=row[0])
				
				EffortInstanceServicesObj.effort_service_description = upfirstletter(hacHeaders[x]);
				
				#classify EffortInstanceServicesObj.effort_service_description based on a dictionary
				EffortInstanceServicesObj.effort_service_type = ServiceType.objects.get(service_name=classify_service_types[EffortInstanceServicesObj.effort_service_description])
				
				EffortInstanceServicesObj.save()


		loc = Location()

		print 'About to convert this lat string to float: '+row[15]
		if(row[15] and row[15] is not '' and row[15] is not ' '):
			latVal = re.sub(r"\D-", "", row[15]).strip()
			print "latVal is "+latVal
			loc.longitude = float(latVal)

		print 'About to convert this long string to float: '+row[16]
		if(row[16] and row[16] is not '' and row[16] is not ' '):
			longVal = re.sub(r"\D-", "", row[16]).strip()
			print "longval is "+longVal
			loc.longitude = float(longVal)
		
		loc.save()
