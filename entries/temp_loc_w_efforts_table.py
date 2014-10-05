# Full path to your django project directory

'''
There is not much of a need to run this anymore since the location custom save function now
creates a new loc_w_efforts row each time a location is saved
'''

your_djangoproject_home="../"

import sys,os
sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hos2.settings'
 
from entries.models import ServiceProvider,Location,EffortInstance,ServiceType,EffortInstanceService,Location_w_efforts
 
for l in Location.objects.all():
    
    print 'printing location id'
    print l.id
    
    #make sure tables are synced up!
    print 'printing date start'
    print EffortInstance.objects.get(location=l.id).date_start
    
    Location_w_effortsObj = Location_w_efforts()
    
    Location_w_effortsObj.date_start = EffortInstance.objects.get(location=l.id).date_start
    
    Location_w_effortsObj.date_end = EffortInstance.objects.get(location=l.id).date_end
    
    Location_w_effortsObj.latitude = l.latitude
    Location_w_effortsObj.longitude = l.longitude
    
    Location_w_effortsObj.id = l.id
    
    provider_num = EffortInstance.objects.get(location=l.id).service_provider
    
    Location_w_effortsObj.service_provider = provider_num
    
    Location_w_effortsObj.provider_name = ServiceProvider.objects.get(service_provider_id=provider_num.service_provider_id).provider_name
    
    Location_w_effortsObj.save()
	



	

