# Full path to your django project directory

your_djangoproject_home="../"

import sys,os
sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hos2.settings'
 
from entries.models import ServiceProvider,Location,EffortInstance,ServiceType,EffortInstanceServices,Location_w_efforts
 
	
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
    
    Location_w_effortsObj.service_provider = EffortInstance.objects.get(location=l.id).service_provider
    
    #ServiceProvider.provider
    #print obj, but need number
    #print 'printing provider number'
    #print provider_num.provider
    
    Location_w_effortsObj.provider_name = ServiceProvider.objects.get(provider=provider_num.provider).provider_name
    
    Location_w_effortsObj.save()
	



	

