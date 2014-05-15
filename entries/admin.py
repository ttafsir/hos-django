from django.contrib import admin
from django.contrib.gis import admin
from models import haiti_adm1_minustah



# Register your models here.
admin.site.register(haiti_adm1_minustah, admin.OSMGeoAdmin)