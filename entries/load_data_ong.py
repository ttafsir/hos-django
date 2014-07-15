# Full path and name to your csv file
csv_filepathname="./data/20140415_ONG_utf8.csv"

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
import unicodedata

#loads the classify_service_types dictionary, used to classify the service types
from service_type_dict import classify_service_types

print classify_service_types

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='~')


#The objects can't have the same name as the class, and a new object needs to be created each time a row is looped through

ongHeaders = ["id","title","Active in Haiti since","Activity","Clinical Services","Contact","Contagious Diseases","Department","Description","Duration","E-mail or phone","Early Intervention","Environmental Health","Gender based violence","HIV-SIDA Infections","Infant Health","Institution","Latitude","Longitude","Maternity Health","Nutrition","Other","Pays","Pychological Health","Re-education","Section","Town"]

# TODO: Need to add column 3 to this below list, but don't know what "arv" means and its not yet in dictionary
ongServiceCols = [4,6,12,13,14,15,19,20,21,23,24]


def upfirstletter(value):
    first = value[0] if len(value) > 0 else ''
    remaining = value[1:] if len(value) > 1 else ''
    return first.upper() + remaining


for row in dataReader:

	#print 'hi5'
	
	if row[0] != 'id': # Ignore the header row, import everything else
		
		
		#print row[0]
		
		EffortInstanceObj = EffortInstance()
		
		print row[2]
		
		if not '0000-' in row[2]:
		
			#might have to add 1 to day field
			#need to add months in duration to date to get end datesets. Therefore may need to work with python date types
			EffortInstanceObj.date_start = row[2]
			
		
		EffortInstanceObj.effort_instance_id = row[0]
		
		
		'''
		if row[33] == 'Hopital' or row[33] == 'CSL' or row[33] == 'CAL':
			#EffortInstanceObj.date_start = '9999-12-31'
			print 'long-term recorded'
			
		if row[33] == 'Hopital':
			EffortInstanceObj.provider_type = 'HL'
			print 'hospital recorded'
		elif row[33] == 'CSL' or row[33] == 'CAL':
			EffortInstanceObj.provider_type = 'CL'
			print 'clinic recorded'
		'''
		
		
		#cool way to make Service Providers unique, if obj does not exist then it creates it.
		#https://docs.djangoproject.com/en/1.6/ref/models/querysets/#get-or-create
		ServiceProviderObj, created = ServiceProvider.objects.get_or_create(provider_name = row[1])
		
		EffortInstanceObj.service_provider = ServiceProvider.objects.get(provider_name=row[1])
		
		loc = Location()

		#having problems with the location strings, must be special non-ASCII characters. ex.
		
		print row[17]
		
		print row[18]
		
		if(len(row[17]) > 1 and not '\\' in row[17] and '.' in row[17]):
			if(len(row[18]) > 1 and not '\\' in row[18] and '.' in row[18]):
		
			
					loc.latitude = row[17].decode('ascii','ignore').replace(" ", "")
					#loc.latitude = '18.305755'
					loc.longitude = row[18].decode('ascii','ignore').replace(" ", "")
					#loc.longitude = '-72.172367'
			
					loc.save()
		
					#LocationObj, created = Location.objects.get_or_create(location_id=row[0],latitude = loc.latitude, longitude = loc.longitude)
			
					
					EffortInstanceObj.location = Location.objects.get(location_id=loc.location_id)
					
					#Location.objects.get(location_id=loc.location_id)
		
			
		EffortInstanceObj.save()
		
		
		for x in ongServiceCols:
			#print "now going through column "+str(x) +" which is "+str(ongHeaders[x])
			#makes sure column has that service type (1 would be the value)
			if row[x] == '1':
			#print row[x]
				#if hacServiceCols[x] != "0":
				#	print "service "+str(x) +" is not equal to 1"
				EffortInstanceServicesObj = EffortInstanceServices()
				
				EffortInstanceServicesObj.effort_instance = EffortInstance.objects.get(effort_instance_id=row[0])
		
				EffortInstanceServicesObj.effort_service_description = upfirstletter(ongHeaders[x].replace("_", " "));
		
				#classify EffortInstanceServicesObj.effort_service_description based on a dictionary
				if ServiceType.objects.filter(service_name=classify_service_types[EffortInstanceServicesObj.effort_service_description]).count() == 1:
					serviceType = ServiceType.objects.get(service_name=classify_service_types[EffortInstanceServicesObj.effort_service_description])
					EffortInstanceServicesObj.effort_service_type = serviceType
		
				EffortInstanceServicesObj.save()
		