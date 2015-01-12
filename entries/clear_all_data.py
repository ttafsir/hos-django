# Full path to your django project directory
your_djangoproject_home="../"

import sys,os
sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hos2.settings'

# http://stackoverflow.com/questions/25537905/django-1-7-throws-django-core-exceptions-appregistrynotready-models-arent-load
# need to add to load installed apps in Django 1.7
import django
django.setup()
 
from entries.models import *

#clears data from all tables except admin tables and temporary tables

ServiceProvider.objects.all().delete()

Location.objects.all().delete()

EffortInstance.objects.all().delete()

ServiceType.objects.all().delete()

EffortInstanceService.objects.all().delete()

Location_w_efforts.objects.all().delete()



 
