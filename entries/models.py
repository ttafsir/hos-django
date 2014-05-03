from django.db import models

class ServiceProvider(models.Model):
	provider =  models.AutoField(primary_key=True)
	provider_name = models.CharField(max_length = 500)

class Location(models.Model):
    #location_id = models.IntegerField(primary_key=True)
    #location_id = models.AutoField(primary_key=True,db_column='location_id')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    #geom = models.TextField(blank=True) # This field type is a guess.
    #address_information = models.CharField(max_length=300, blank=True)
        
class EffortInstance(models.Model):
	'''
	TRAVELING_TEAM = 'TT'
	CLINIC = 'CL'
	HOSPITAL = 'HL'
	PROVIDER_TYPE_OPTIONS = (
		(TRAVELING_TEAM, 'Traveling Team'),
		(CLINIC, 'Clinic'),
		(HOSPITAL, 'Hospital'),
	)
	'''
	#effort_instance =  models.AutoField(primary_key=True)
	effort_instance_id =  models.IntegerField(primary_key=True)
	#service_provider = models.ForeignKey('ServiceProvider')
	#provider_type = models.CharField(max_length=2, choices=PROVIDER_TYPE_OPTIONS, default=CLINIC)
	date_start = models.DateTimeField(auto_now=False)
	#date_end = models.DateTimeField(auto_now=False)
	
class ServiceType(models.Model):
    service_type_id = models.IntegerField(primary_key=True)
    #service_type_test_id = models.IntegerField(blank=True, null=True)
    service_name = models.CharField(max_length=100, blank=True)
    service_description = models.CharField(max_length=300, blank=True)
	
class EffortInstanceServices(models.Model):
    effort_instance_service_id = models.IntegerField(primary_key=True)
    effort_instance = models.ForeignKey(EffortInstance, blank=True, null=True)
    effort_service_type = models.ForeignKey('ServiceType', blank=True, null=True)
    effort_service_description = models.CharField(max_length=300, blank=True)
