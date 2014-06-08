HOS-Django
===========

HopeOneSource Geospatial Database

This project consists of a GeoDjango implementation of a PostGIS database. The HOS database
models health facilities in Haiti including their locations and the services they provide.

The file structure shown follows the typical Django file structure. Keep in mind GeoDjango
functionality is enabled. Also this project connects to a PostGIS database.

The haiti_geospatial_data folder consists of shapefiles used for a web map.

The notes folder contains relevant notes, but nothing the code is dependent on.

Description of folders:

hos2 folder:

- settings.py: Notice that GeoDjango django.contrib.gis app is included. Also 
that other databases can be connected to by uncommenting the appropriate code block. This 
makes it easy to switch from a local database to a shared database

entries folder:

- 




How to load geospatial data into hos1 database:

Invoke the Django shell from the geodjango project directory:

$ python manage.py shell

Next, import the load_geospatial_data module, call the run routine, and watch LayerMapping do the work:

>>> from entries import load_geospatial_data
>>> load_geospatial_data.run()




