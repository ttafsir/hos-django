from django.db import models

class ServiceProvider(models.Model):
	provider =  models.AutoField(primary_key=True)
	provider_name = models.CharField(max_length = 200)

class EffortInstance(models.Model):
	TRAVELING_TEAM = 'TT'
	CLINIC = 'CL'
	HOSPITAL = 'HL'
	PROVIDER_TYPE_OPTIONS = (
		(TRAVELING_TEAM, 'Traveling Team'),
		(CLINIC, 'Clinic'),
		(HOSPITAL, 'Hospital'),
	)
	effort_instance =  models.AutoField(primary_key=True)
	service_provider = models.ForeignKey('ServiceProvider')
	provider_type = models.CharField(max_length=2, choices=PROVIDER_TYPE_OPTIONS, default=CLINIC)
	date_start = models.DateTimeField(auto_now=False)
	date_end = models.DateTimeField(auto_now=False)
	
class EffortInstanceServices(models.Model):
	TRAVELING_TEAM = 'TT'
	CLINIC = 'CL'
	HOSPITAL = 'HL'
	PROVIDER_TYPE_OPTIONS = (
		(TRAVELING_TEAM, 'Traveling Team'),
		(CLINIC, 'Clinic'),
		(HOSPITAL, 'Hospital'),
	)
	effort_instance =  models.AutoField(primary_key=True)
	service_provider = models.ForeignKey('ServiceProvider')
	provider_type = models.CharField(max_length=2, choices=PROVIDER_TYPE_OPTIONS, default=CLINIC)
	date_start = models.DateTimeField(auto_now=False)
	date_end = models.DateTimeField(auto_now=False)