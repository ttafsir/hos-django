from django.db import models
#extra stuff for GeoDjango
from django.contrib.gis.db import models as geomodels
from django.contrib.gis.geos import *

objects = geomodels.GeoManager()

class ServiceProvider(models.Model):
	provider =  models.AutoField(primary_key=True)
	provider_name = models.CharField(max_length = 500)

class Location(models.Model):
    location_id = models.AutoField(primary_key=True,db_column='location_id')
    #latitude and longitude need to be changed to string types for GeoDjango
    latitude = models.CharField(max_length=15, blank=True, null=True)
    longitude = models.CharField(max_length=15, blank=True, null=True)  
    geom = geomodels.PointField(dim=3, geography=True, blank=True, null=True)
    #address_information = models.CharField(max_length=300, blank=True)
    
def save(self):
	if self.latitude != None and len(self.latitude) > 0:
		lString = 'POINT(%s %s)' % (self.longitude.strip(), self.latitude.strip())
		self.point = fromstr(lString)
	self.last_modified = datetime.now()
	super(Band, self).save()
	        
class EffortInstance(models.Model):
	TRAVELING_TEAM = 'TT'
	CLINIC = 'CL'
	HOSPITAL = 'HL'
	PROVIDER_TYPE_OPTIONS = (
		(TRAVELING_TEAM, 'Traveling Team'),
		(CLINIC, 'Clinic'),
		(HOSPITAL, 'Hospital'),
	)
	
	#effort_instance =  models.AutoField(primary_key=True)
	effort_instance_id =  models.IntegerField(primary_key=True)
	service_provider = models.ForeignKey(ServiceProvider, blank=True, null=True)
	location = models.ForeignKey(Location, blank=True, null=True)
	provider_type = models.CharField(max_length=2, choices=PROVIDER_TYPE_OPTIONS, default=CLINIC)
	date_start = models.DateTimeField(auto_now=False, null=True)
	date_end = models.DateTimeField(auto_now=False, null=True)
	
class ServiceType(models.Model):
    service_type_id = models.IntegerField(primary_key=True)
    service_name = models.CharField(max_length=100, blank=True)
    service_description = models.CharField(max_length=300, blank=True)
	
class EffortInstanceServices(models.Model):
    #effort_instance_service_id = models.IntegerField(primary_key=True)
    effort_instance_service_id = models.AutoField(primary_key=True)
    effort_instance = models.ForeignKey(EffortInstance, blank=True, null=True)
    effort_service_type = models.ForeignKey('ServiceType', blank=True, null=True)
    effort_service_description = models.CharField(max_length=300, blank=True)
