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

FAQ:

Why do I have trouble importing CSVs from my mac to Github?

On a Mac, Excel produces csv files with the wrong line endings, which causes problems for git (amongst other things).
see: http://nicercode.github.io/blog/2013-04-30-excel-and-line-endings/

For me, the issue importing CSV files on a Mac is that the importer doesn't support the default mac "record separator" (the line ending).
On a mac, the default line eding is CR (carriage return).
Unix line endings (LF: line feed) and Windows line endings (CRLF) are supported.
Changing the line ending of your csv file to eg. CR will make QGIS import the file just fine (I used TextWrangler).
(http://hub.qgis.org/issues/8421)


Sources:

Geospatial Data: 

http://www.gvsu.edu/haitiwater/links-to-gis-data-for-haiti-9.htm

Scrapped Data:

MMEX:
www.mmex.org/missions?tid=1&tid_1=All&items_per_page=All&views_exposed_form_focused_field

HAC:
http://www.mspp.gouv.ht/cartographie/index.php#

ONG:
http://www.mspp.gouv.ht/cartographie/detail_ong.php?idInstitution=$popup

Haiti Aid Map:
haiti.ngoaidmap.org/




