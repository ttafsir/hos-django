# Full path and name to your csv file

#csv_filepathname="/Users/thomasgertin1/hos-django/entries/20140415_HAC_utf8.csv"
csv_filepathname="./20140415_HAC_utf8.csv"

# Full path to your django project directory

#your_djangoproject_home="/Users/thomasgertin1/hos-django/"
# two directories up. Chained!
your_djangoproject_home="../../hos-django/"
 
import sys,os
sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hos2.settings'
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hos2.settings")
 
from entries.models import ServiceProvider,Location,EffortInstance,ServiceType,EffortInstanceServices
 
import csv

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
 
for row in dataReader:

	print 'hi'
	
	if row[0] != 'id': # Ignore the header row, import everything else
		
		ServiceType = ServiceType()
		#ServiceType.service_type_id = row[0]
		ServiceType.service_name = row[1]
		ServiceType.service_description = row[6]
		ServiceType.save()
	
	
	'''
		EffortInstanceServices = EffortInstanceServices()
		#EffortInstanceServices.effort_instance_service_id = row[0]
		EffortInstanceServices.effort_service_description = row[1]
		EffortInstanceServices.save()
	'''
	
	print 'bye'
	
	
	

'''
if row[0] != 'ZIPCODE': # Ignore the header row, import everything else
zipcode = ZipCode()
zipcode.zipcode = row[0]
zipcode.city = row[1]
zipcode.statecode = row[2]
zipcode.statename = row[3]
zipcode.save()
'''