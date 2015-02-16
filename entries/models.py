from django.db import models
from django.db.models import signals
#extra stuff for GeoDjango
from django.contrib.gis.db import models
from django.contrib.gis.geos import *

class ServiceProvider(models.Model):
	service_provider_id =  models.AutoField(primary_key=True)
	provider_name = models.CharField(max_length = 500)
	#provider_name_en = models.CharField(max_length = 500)
	#provider_name_fr = models.CharField(max_length = 500)
	#provider_name_cr = models.CharField(max_length = 500)

class Location(models.Model):
	#latitude and longitude need to be changed to string types for GeoDjango
	latitude = models.CharField(max_length=15, blank=True, null=True)
	longitude = models.CharField(max_length=15, blank=True, null=True) 

	#overriding the default manager with a GeoManager instance. 
	#Changing geography to equal False, and dim(dimension to 2) This will use a geom type and be compatible with the admin polygons
	geom = models.PointField(dim=2, geography=False, blank=True, null=True)
	objects = models.GeoManager()

	def save(self,input_id):
		if self.latitude != None and len(self.latitude) > 0:
			lString = 'POINT(%s %s)' % (self.longitude.strip(), self.latitude.strip())
			self.geom = fromstr(lString)
		super(Location, self).save()

		if self.latitude != None and len(self.latitude) > 0:
			#whenever a location is saved, it creates a new tuple for the Location_w_efforts table, to keep the table up to date
			Location_w_effortsObj = Location_w_efforts()
			Location_w_effortsObj.provider_name = 'test1'
			Location_w_effortsObj.latitude = self.latitude
			Location_w_effortsObj.longitude = self.longitude
			Location_w_effortsObj.id = self.id
			Location_w_effortsObj.date_start = EffortInstance.objects.get(effort_instance_id=input_id).date_start
			Location_w_effortsObj.date_end = EffortInstance.objects.get(effort_instance_id=input_id).date_end
			provider_num = EffortInstance.objects.get(effort_instance_id=input_id).service_provider
			Location_w_effortsObj.service_provider = provider_num
			Location_w_effortsObj.provider_name = ServiceProvider.objects.get(service_provider_id=provider_num.service_provider_id).provider_name
			Location_w_effortsObj.save()
		
class haiti_adm1_minustah(models.Model):
    id_adm1 = models.FloatField()
    adm1 = models.CharField(max_length=45)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.adm1

class haiti_adm2_minustah(models.Model):
    id_adm1 = models.FloatField()
    adm1 = models.CharField(max_length=45)
    id_adm2 = models.FloatField()
    adm2 = models.CharField(max_length=45)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    pop = models.IntegerField()
    sq_miles = models.FloatField()
    pop_sq_mi = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.adm2
        
class haiti_adm3_minustah(models.Model):
    id_adm1 = models.FloatField()
    adm1 = models.CharField(max_length=45)
    id_adm2 = models.FloatField()
    adm2 = models.CharField(max_length=45)
    id_adm3 = models.FloatField()
    nom_adm3 = models.CharField(max_length=45)
    adm3 = models.CharField(max_length=45)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.adm3
        
class haiti_adm4_minustah(models.Model):
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    id_adm1 = models.FloatField()
    adm1 = models.CharField(max_length=45)
    id_adm2 = models.FloatField()
    adm2 = models.CharField(max_length=45)
    id_adm3 = models.FloatField()
    nom_adm3 = models.CharField(max_length=45)
    adm3 = models.CharField(max_length=45)
    no_adm4 = models.FloatField()
    id_adm4 = models.CharField(max_length=45)
    nom_adm4 = models.CharField(max_length=45)
    adm4 = models.CharField(max_length=45)
    shape_le_1 = models.FloatField()
    shape_ar_1 = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.adm4

class Common_EffortInstance_Info(models.Model):
	TRAVELING_TEAM = 'TT'
	CLINIC = 'CL'
	HOSPITAL = 'HL'
	TYPE_OPTIONS = (
		(TRAVELING_TEAM, 'Traveling Team'),
		(CLINIC, 'Clinic'),
		(HOSPITAL, 'Hospital'),
	)
	
	#effort_instance_id =  models.IntegerField(primary_key=True)
	service_provider = models.ForeignKey(ServiceProvider, blank=True, null=True)
	type = models.CharField(max_length=2, choices=TYPE_OPTIONS, default=CLINIC)
	date_start = models.DateTimeField(auto_now=False, null=True)
	date_end = models.DateTimeField(auto_now=False, null=True)
	default = models.NullBooleanField(primary_key=False, blank=True)
	description = models.CharField(max_length=600, blank=True)
	
	drupal_id = models.IntegerField(default=0)
	
	class Meta:
		abstract = True
        
class EffortInstance(Common_EffortInstance_Info):
	effort_instance_id =  models.IntegerField(primary_key=True)
	updated_on = models.DateTimeField(auto_now=False, null=True)
	updated_by = models.CharField(max_length=100, blank=True)
	#location = models.ForeignKey(Location,blank=True, null=True)
	#change Location to One-to-one relationship: https://docs.djangoproject.com/en/1.7/topics/db/examples/one_to_one/
	location = models.OneToOneField(Location,blank=True, null=True)
	adm_1 = models.ForeignKey(haiti_adm1_minustah, blank=True, null=True)
	adm_2 = models.ForeignKey(haiti_adm2_minustah, blank=True, null=True)
	adm_3 = models.ForeignKey(haiti_adm3_minustah, blank=True, null=True)
	
class ServiceType(models.Model):
    service_type_id = models.IntegerField(primary_key=True)
    service_name_en = models.CharField(max_length=100, blank=True)
    service_name_fr = models.CharField(max_length=100, blank=True)
    service_name_cr = models.CharField(max_length=100, blank=True)
    #service_description = models.CharField(max_length=300, blank=True)
    
class EffortInstanceService(models.Model):
    effort_instance_service_id = models.AutoField(primary_key=True)
    effort_instance = models.ForeignKey(EffortInstance, blank=True, null=True)
    effort_service_type = models.ForeignKey('ServiceType', blank=True, null=True)
    #effort_service_description = models.CharField(max_length=300, blank=True)
    
#temporary model to display points along with their associated effort instance and service provider
#inherits from the Common_EffortInstance_Info base class
class Location_w_efforts(Common_EffortInstance_Info):
	
	provider_name = models.CharField(max_length = 500)
	
	#you don't need location_id below because you have location field above
	#location_id = models.IntegerField(primary_key=False)
	#latitude and longitude need to be changed to string types for GeoDjango
	latitude = models.CharField(max_length=15, blank=True, null=True)
	longitude = models.CharField(max_length=15, blank=True, null=True) 

	#overriding the default manager with a GeoManager instance. 
	geom = models.PointField(dim=3, geography=True, blank=True, null=True)
	
	objects = models.GeoManager()
	
	def save(self):
		if self.latitude != None and len(self.latitude) > 0:
			lString = 'POINT(%s %s)' % (self.longitude.strip(), self.latitude.strip())
			self.geom = fromstr(lString)
		super(Location_w_efforts, self).save()
		
#table to store the spatial clusters results
class Spatial_cluster_results(Common_EffortInstance_Info):

	#effort_instance = models.ForeignKey(EffortInstance, blank=True, null=True)
	effort_instance_id =  models.IntegerField(primary_key=False)
	
	provider_name = models.CharField(max_length = 500)
	
	nearby_points = models.IntegerField(primary_key=False, blank=True, null=True)
	point_checked = models.NullBooleanField(primary_key=False, blank=True)
	
	latitude = models.CharField(max_length=15, blank=True, null=True)
	longitude = models.CharField(max_length=15, blank=True, null=True) 

	#overriding the default manager with a GeoManager instance. 
	geom = models.PointField(dim=3, geography=True, blank=True, null=True)
	objects = models.GeoManager()
	
	def save(self):
		if self.latitude != None and len(self.latitude) > 0:
			lString = 'POINT(%s %s)' % (self.longitude.strip(), self.latitude.strip())
			self.point = fromstr(lString)
		super(Spatial_cluster_results, self).save()
		
#table to store the admin3 point in polygon processing
class Admin_cluster_results(Common_EffortInstance_Info):

	provider_name = models.CharField(max_length = 500)
	
	nearby_points = models.IntegerField(primary_key=False, blank=True, null=True)
	point_checked = models.NullBooleanField(primary_key=False, blank=True)
	
	latitude = models.CharField(max_length=15, blank=True, null=True)
	longitude = models.CharField(max_length=15, blank=True, null=True) 

	#overriding the default manager with a GeoManager instance. 
	geom = models.PointField(dim=3, geography=True, blank=True, null=True)
	objects = models.GeoManager()
	
	def save(self):
		if self.latitude != None and len(self.latitude) > 0:
			lString = 'POINT(%s %s)' % (self.longitude.strip(), self.latitude.strip())
			self.point = fromstr(lString)
		super(Admin_cluster_results, self).save()
		
class Similar_strings(models.Model):
	similar_strings_id = models.AutoField(primary_key=True)
	#effort_instance_id = models.ForeignKey(Spatial_cluster_results, blank=True, null=True)
	string_id = models.IntegerField(primary_key=False, blank=True, null=True)
	provider_name = models.CharField(max_length = 500)
	related_string_id = models.IntegerField(primary_key=False, blank=True, null=True)
	related_provider_name = models.CharField(max_length = 500)
	similarity_score = models.DecimalField(max_digits=15, decimal_places=13)