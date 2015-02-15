HOS-Django
===========

HopeOneSource GeoDjango Project

This project consists of a GeoDjango implementation modeling health facilities in Haiti including their locations
and the services they provide.

The file structure shown follows the typical Django file structure. Keep in mind GeoDjango
functionality is enabled. Also, this project connects to a PostGIS database.

Description of folders:

The haiti_geospatial_data folder consists of shapefiles used for a web map.

The notes folder contains relevant notes, but nothing the code is dependent on.

The packer folder contains a json packer template that can be used to set-up an Ubuntu server will all the required dependencies for hos-django

hos2 folder:

- settings.py: Notice that GeoDjango django.contrib.gis app is included. Also 
that other databases can be connected to by uncommenting the appropriate code block. This 
makes it easy to switch from a local database to a shared database

- entries folder: The entries folder contains a data folder
that contains the CSVs that will be imported, all of the relevant python scripts to load data into PostGIS, 
and the templates folder that contains the templates for the views

The Python scripts in the entries folder:

- load data scripts: There are four individual scripts that load data from the four separate CSV files that are in the 
data folder (However there are 3 separate data sources). The scripts are load_data_hac.py, load_data_ong.py, load_data_mmex.py, and load_data_haiti_aid_map.py. Each of
these scripts loads that data into the appropriate table in the HOS database and creates the proper relations. A user can run these four scripts individually or run the load_all_data.py 
script to load all of the data into the geodatabase. 

- load_Service_Type_table.py must be run before the load data scripts. It populates the ServiceType table with all of the possible services, and this table needs to be populated so 
the necessary relations are created when the load data scripts are run.

- clear_all_data.py script clears all of the data in the database.

- service_type_dictionary.py is just a dictionary that the load data scripts import in order to related different entries that show up as services in the individual datasets so that they can be 
classified into one of the standard service types defined in the ServiceType table.

- load_geospatial_data.py loads the admin shapefiles found in the haiti_geospatial_data folder and imports them as polygons in the 
HOS1 geodatabase. This only needs to be run once after the database is created.

- The adm1_name_dict.py, adm2_name_dict.py, and adm3_name_dict.py are dictionaries so that the different entries in the individual datasets for admin areas can be 
classified to the admin names found in the respective haiti_admin tables.

- temp_loc_w_efforts_table.py produces a temporary table that has all of the location points and appends the 
start date, end date, and provider name.

- admin3_list.py: might be an intermediary file that isn't used anymore?

- deduplicate_database.py: find possible effort instances that might be duplicates based on spatial proximity and string similarity.


How to load geospatial data into hos1 database:

Invoke the Django shell from the geodjango project directory:

$ python manage.py shell

Next, import the load_geospatial_data module, call the run routine, and watch LayerMapping do the work:

>>> from entries import load_geospatial_data
>>> load_geospatial_data.run()


Dependencies

-pip install django-leaflet


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

Scraped Data:

MMEX:
www.mmex.org/missions?tid=1&tid_1=All&items_per_page=All&views_exposed_form_focused_field

HAC:
http://www.mspp.gouv.ht/cartographie/index.php#

ONG:
http://www.mspp.gouv.ht/cartographie/detail_ong.php?idInstitution=$popup

Haiti Aid Map:
haiti.ngoaidmap.org/




