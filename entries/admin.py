from django.contrib import admin
from django.contrib.gis import admin
from models import haiti_adm1_minustah, haiti_adm2_minustah, haiti_adm3_minustah, haiti_adm4_minustah, Location



# Register your models here.
admin.site.register(haiti_adm1_minustah, admin.OSMGeoAdmin)
admin.site.register(haiti_adm2_minustah, admin.OSMGeoAdmin)
admin.site.register(haiti_adm3_minustah, admin.OSMGeoAdmin)
admin.site.register(haiti_adm4_minustah, admin.OSMGeoAdmin)
admin.site.register(Location, admin.OSMGeoAdmin)