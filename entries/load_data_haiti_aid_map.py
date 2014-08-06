# Full path and name to your csv file

csv_filepathname="./data/20140413_Haiti_Aid_Map_utf8.csv"

# Full path to your django project directory

your_djangoproject_home="../"

import sys,os
sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hos2.settings'
 
from entries.models import ServiceProvider,Location,EffortInstance,ServiceType,EffortInstanceServices,haiti_adm1_minustah,haiti_adm2_minustah,haiti_adm3_minustah
 
import csv
#module used for regular expressions
import re
import random

#loads the classify_service_types dictionary, used to classify the service types
from service_type_dict import classify_service_types

#loads the classify_adm1_names dictionary, used to classify the admin 1 boundaries
from adm1_name_dict import classify_adm1_names

#loads the classify_adm2_names dictionary, used to classify the admin 2 boundaries
from adm2_name_dict import classify_adm2_names

#loads the classify_adm2_names dictionary, used to classify the admin 2 boundaries
from adm3_name_dict import classify_adm3_names

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
 
#The objects can't have the same name as the class, and a new object needs to be created each time a row is looped through

'''
I need two functions, one that fills all the tables with the right info for each effort instance. The other one
will just fill in the location information and have the ability to call the first function multiple time even for each row
'''

def FillTables(locationOrder,adm2Bool,adm3Bool):

	if row[0] != 'id': # Ignore the header row, import everything else
	
		#checks to see if sector category is health
		if re.search('Health',row[12]):
		
			print 'row: id:'
			print row[0]
			
			EffortInstanceObj = EffortInstance()
		
			EffortInstanceObj.effort_instance_id = row[0]
			
			if locationOrder == 2:
			
				EffortInstanceObj.effort_instance_id = row[0] + '02'
			
			if locationOrder == 3:
			
				EffortInstanceObj.effort_instance_id = row[0] + '03'
		

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
		
			#HaitiAipMap does not have any lat lon coords, so don't add a location point
			#Also, don't use random lat lon. It will break spatial queries
			
			#loc = Location()
		
			#loc.latitude = str(random.randint(0,10))
		
			#loc.longitude = str(random.randint(0,10))
		
			#loc.save()
		
			'''
			Insert new code here to match admin boundaries: The location_information column is in column 21 (row [20]). This contains a list
			of admin boundaries where the facility is located at. The list contains entries delimited with '>'. The first entry on the list is Haiti. 
			The second entry is an admin 2 boundary. The third entry is ?.
			
			There can be more than one place listed in the location column. If this is the case then we need to create a new effort instance
			for each location in Haiti.
			'''
		
			if row[20]:
			
				split_each_location = re.split(r'\|Haiti>', row[20].strip())
				
	
				if len(split_each_location) > 1:
					split_loc = re.split(r'>', split_each_location[locationOrder].strip())
			
					if len(split_loc) > 1:

						UpperAdmin1 = split_loc[0].upper()
					
						UpperAdmin1 = re.split(r'\|', UpperAdmin1)
						
						print 'length of split_loc:'
						
						print len(split_loc)
		
						print 'UpperAdmin1:'
						
						print UpperAdmin1[0]
					
						EffortInstanceObj.adm_1 = haiti_adm1_minustah.objects.get(adm1=classify_adm1_names[UpperAdmin1[0]])
					
						if len(split_loc) > 1:
					
							UpperAdmin2 = split_loc[1].upper()
						
							UpperAdmin2 = re.split(r'\|', UpperAdmin2)
							
							print 'UpperAdmin2:'
						
							print UpperAdmin2[0]
						
							try:
			
								EffortInstanceObj.adm_2 = haiti_adm2_minustah.objects.get(adm2=classify_adm2_names[UpperAdmin2[0]])
				
							except:
			
								print "guess no match"
							
							
							if len(split_loc) > 2:
					
								UpperAdmin3 = split_loc[2].upper()
						
								UpperAdmin3 = re.split(r'\|', UpperAdmin3)
								
								print 'UpperAdmin3:'
						
								print UpperAdmin3[0]
	
						
								try:
			
									EffortInstanceObj.adm_3 = haiti_adm3_minustah.objects.get(adm3=classify_adm3_names[UpperAdmin3[0]])
				
								except:
			
									print "guess no match"
								

	
			#need a way first in seeing if a location exists close by
			#EffortInstanceObj.location = loc.objects.get
			EffortInstanceObj.save()
			
			
			
			if len(split_each_location) > 1:
				print 'location 1:'
				print split_each_location[1]
				
			if len(split_each_location) > 2 and adm2Bool == False:
				print 'location 2:'
				print split_each_location[2]
				FillTables(2,True,False)
				
			if len(split_each_location) > 3 and adm3Bool == False and adm2Bool == True:
				print 'location 3:'
				print split_each_location[3]
				FillTables(3,True,True)
		

for row in dataReader:

	FillTables(1,False,False)
		
	
	

