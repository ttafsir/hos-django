from django.contrib.gis.db import models
from django.contrib.gis.gdal import DataSource

your_djangoproject_home="../"

import sys,os
sys.path.append(your_djangoproject_home)

#os.environ['DJANGO_SETTINGS_MODULE'] = 'hos2.settings'

from django.contrib.gis.utils import LayerMapping
from entries.models import haiti_adm1_minustah
 
haiti_adm1_minustah_mapping = {
    'id_adm1' : 'ID_ADM1',
    'adm1' : 'ADM1',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

#haiti_adm1_minustah_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), './haiti_geospatial_data/haiti_adm1_minustah.shp'))
haiti_adm1_minustah_shp = '/Users/thomasgertin1/hos-django/haiti_geospatial_data/haiti_adm1_minustah.shp'

def run(verbose=True):
	#initially made dumb error of having haiti_adm1_minustah and haiti_adm1_minustah_shp named the same
    lm = LayerMapping(haiti_adm1_minustah, haiti_adm1_minustah_shp, haiti_adm1_minustah_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)