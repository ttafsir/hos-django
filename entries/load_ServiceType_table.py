# Full path and name to your csv file

#csv_filepathname="/Users/thomasgertin1/hos-django/entries/20140415_HAC_utf8.csv"
#csv_filepathname="./data/20140419_mmex_utf8.csv"

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

#dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
 
ServiceType = ServiceType()

#create list
services = ['Cardiovascular',
'Dental',
'Diabetes',
'Emergency', 
'General consultation',
'Hypertension',
'Intensive care',
'Laboratory',
'Malaria',
'ORL', 
'ObGyn',
'Operating room',
'Palliative care',
'Pediatrics',
'Pharmacy',
'Physical therapy',
'Free obstetric care program',   
'Psychology Service',
'Surgery',
'Vaccination (PEV)',
'Clinical Services',
'Contagious Diseases',
'Environmental Health',
'Gender based violence',
'HIV-SIDA Infections',
'Infant Health',
'Maternity Health',
'Nutrition',
'Re-education',
'EyeCare',
'Not Classified']

count = 1

for x in range(0,len(services)):

	ServiceType.service_type_id = count
	ServiceType.service_name = services[x]
	
	count = count + 1


	ServiceType.save()


