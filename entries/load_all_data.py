# Full path to your django project directory
your_djangoproject_home="../"

import sys,os
sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hos2.settings'
 
#loads all data from three datasets

if (True):
	import entries.load_ServiceType_table
	
if (True):
	import entries.load_data_hac
	
if (True):
	import entries.load_data_ong
	
if (True):
	import entries.load_data_mmex
	
if (True):
	import entries.load_data_haiti_aid_map





 
