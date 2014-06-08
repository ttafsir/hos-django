from django.contrib.gis.db import models
from django.contrib.gis.gdal import DataSource

your_djangoproject_home="../"

# https://docs.djangoproject.com/en/1.5/ref/contrib/gis/tutorial/

import sys,os
sys.path.append(your_djangoproject_home)

#os.environ['DJANGO_SETTINGS_MODULE'] = 'hos2.settings'

from django.contrib.gis.utils import LayerMapping
from entries.models import haiti_adm1_minustah
from entries.models import haiti_adm2_minustah
from entries.models import haiti_adm3_minustah
from entries.models import haiti_adm4_minustah
 
haiti_adm1_minustah_mapping = {
    'id_adm1' : 'ID_ADM1',
    'adm1' : 'ADM1',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

haiti_adm2_minustah_mapping = {
    'id_adm1' : 'ID_ADM1',
    'adm1' : 'ADM1',
    'id_adm2' : 'ID_ADM2',
    'adm2' : 'ADM2',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'pop' : 'pop',
    'sq_miles' : 'sq_miles',
    'pop_sq_mi' : 'pop_sq_mi',
    'geom' : 'MULTIPOLYGON',
}

haiti_adm3_minustah_mapping = {
    'id_adm1' : 'ID_ADM1',
    'adm1' : 'ADM1',
    'id_adm2' : 'ID_ADM2',
    'adm2' : 'ADM2',
    'id_adm3' : 'ID_ADM3',
    'nom_adm3' : 'NOM_ADM3',
    'adm3' : 'ADM3',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

haiti_adm4_minustah_mapping = {
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'id_adm1' : 'ID_ADM1',
    'adm1' : 'ADM1',
    'id_adm2' : 'ID_ADM2',
    'adm2' : 'ADM2',
    'id_adm3' : 'ID_ADM3',
    'nom_adm3' : 'NOM_ADM3',
    'adm3' : 'ADM3',
    'no_adm4' : 'NO_ADM4',
    'id_adm4' : 'ID_ADM4',
    'nom_adm4' : 'NOM_ADM4',
    'adm4' : 'ADM4',
    'shape_le_1' : 'Shape_Le_1',
    'shape_ar_1' : 'Shape_Ar_1',
    'geom' : 'MULTIPOLYGON',
}


#http://stackoverflow.com/questions/9271464/what-does-the-file-wildcard-mean-do
#haiti_adm1_minustah_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), './haiti_geospatial_data/haiti_adm1_minustah.shp'))
haiti_adm1_minustah_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../haiti_geospatial_data/haiti_adm1_minustah.shp'))
haiti_adm2_minustah_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../haiti_geospatial_data/haiti_adm2_minustah.shp'))
haiti_adm3_minustah_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../haiti_geospatial_data/haiti_adm3_minustah.shp'))
haiti_adm4_minustah_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../haiti_geospatial_data/haiti_adm4_minustah.shp'))


def run(verbose=True):
	#initially made dumb error of having haiti_adm1_minustah and haiti_adm1_minustah_shp named the same
    lm_adm1 = LayerMapping(haiti_adm1_minustah, haiti_adm1_minustah_shp, haiti_adm1_minustah_mapping,
                      transform=False, encoding='iso-8859-1')

    lm_adm1.save(strict=True, verbose=verbose)
    
    lm_adm2 = LayerMapping(haiti_adm2_minustah, haiti_adm2_minustah_shp, haiti_adm2_minustah_mapping,
                      transform=False, encoding='iso-8859-1')

    lm_adm2.save(strict=True, verbose=verbose)
    
    lm_adm3 = LayerMapping(haiti_adm3_minustah, haiti_adm3_minustah_shp, haiti_adm3_minustah_mapping,
                      transform=False, encoding='iso-8859-1')

    lm_adm3.save(strict=True, verbose=verbose)
    
    lm_adm4 = LayerMapping(haiti_adm4_minustah, haiti_adm4_minustah_shp, haiti_adm4_minustah_mapping,
                      transform=False, encoding='iso-8859-1')

    lm_adm4.save(strict=True, verbose=verbose)
    
    
#load_geospatial_data.run()
