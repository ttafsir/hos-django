HOS-Django
===========

###HopeOneSource GeoDjango Project

This project consists of a GeoDjango implementation modeling health facilities in Haiti including their locations
and the services they provide.

##RESTful API:

###GET find/

Give a lat/lon pair, and an optional buffer distance in meters. Returns the health facilities surrounding it.

Example:

http://example.org/find/?lat=18.57&lon=-72.293&buffer=1000

response:

{
    "crs": {
        "type": "link",
        "properties": {
            "href": "http://spatialreference.org/ref/epsg/4326/",
            "type": "proj4"
        }
    },
    "type": "FeatureCollection",
    "features": [
        {
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -72.2915,
                    18.5704
                ]
            },
            "type": "Feature",
            "properties": {
                "description": "",
                "similarity": "nearby",
                "default": null,
                "date_end": null,
                "date_start": null,
                "longitude": "-72.2915",
                "drupal_id": 0,
                "latitude": "18.5704",
                "provider_name": "CHOSCAL",
                "service_provider": 7419,
                "type": "CL",
                "model": "entries.location_w_efforts_temp"
            },
            "id": 11971
        }
    ]
}


###GET all/

Returns all health facilities in database.

Example:

http://example.org/find/all/


###GET /entries/<pk>/results/

Returns other what services the requested health facility provides. Insert the EffortInstance ID for <pk>

Example:

http://example.org/entries/11887/results/

response:

["General consultation", "Pediatrics", "Malaria", "Emergency", "Physical therapy", "Vaccination (PEV)", "Dental", "Pharmacy", "Operating room", "Obstetric care", "Palliative care", "Hypertension", "Laboratory", "Cardiovascular", "Psychology service", "ObGyn", "Diabetes"]


###GET /entries/shared_servicetype/

Returns other health facilities that offer the same type of services.

Example:

http://example.org/entries/shared_servicetype/?id=11779

response:

{'effort_instance_id': 221810}{'effort_instance_id': 221818}{'effort_instance_id': 221542}{'effort_instance_id': 221983}{'effort_instance_id': 33009}{'effort_instance_id': 221732}{'effort_instance_id': 221834}{'effort_instance_id': 221991}{'effort_instance_id': 33089}{'effort_instance_id': 221754}{'effort_instance_id': 221865}{'effort_instance_id': 221809}{'effort_instance_id': 221871}{'effort_instance_id': 221869}{'effort_instance_id': 22409}{'effort_instance_id': 221830}{'effort_instance_id': 221984}{'effort_instance_id': 33102}{'effort_instance_id': 33134}{'effort_instance_id': 221533}{'effort_instance_id': 221870}{'effort_instance_id': 221543}{'effort_instance_id': 33034}{'effort_instance_id': 221757}{'effort_instance_id': 221832}{'effort_instance_id': 221825}{'effort_instance_id': 22410}{'effort_instance_id': 221873}{'effort_instance_id': 221868}{'effort_instance_id': 221858}{'effort_instance_id': 33127}{'effort_instance_id': 33104}{'effort_instance_id': 221954}{'effort_instance_id': 33142}{'effort_instance_id': 22165}{'effort_instance_id': 221996}{'effort_instance_id': 221957}{'effort_instance_id': 33043}{'effort_instance_id': 221867}{'effort_instance_id': 33045}{'effort_instance_id': 221821}{'effort_instance_id': 33095}{'effort_instance_id': 221982}{'effort_instance_id': 33123}{'effort_instance_id': 22951}{'effort_instance_id': 221859}{'effort_instance_id': 221736}{'effort_instance_id': 221864}{'effort_instance_id': 222007}{'effort_instance_id': 221819}{'effort_instance_id': 33118}{'effort_instance_id': 221725}{'effort_instance_id': 221827}{'effort_instance_id': 221861}{'effort_instance_id': 221737}{'effort_instance_id': 33100}{'effort_instance_id': 22952}{'effort_instance_id': 221862}{'effort_instance_id': 221833}{'effort_instance_id': 33048}{'effort_instance_id': 221817}{'effort_instance_id': 221815}{'effort_instance_id': 221951}{'effort_instance_id': 22950}{'effort_instance_id': 33116}{'effort_instance_id': 221955}{'effort_instance_id': 221829}{'effort_instance_id': 221826}{'effort_instance_id': 221866}{'effort_instance_id': 221828}{'effort_instance_id': 221831}{'effort_instance_id': 221811}{'effort_instance_id': 33010}{'effort_instance_id': 221529}{'effort_instance_id': 221822}{'effort_instance_id': 22408}{'effort_instance_id': 221863}{'effort_instance_id': 221824}{'effort_instance_id': 33026}{'effort_instance_id': 221872}{'effort_instance_id': 221714}{'effort_instance_id': 221875}{'effort_instance_id': 221816}{'effort_instance_id': 33137}{'effort_instance_id': 221981}{'effort_instance_id': 221734}{'effort_instance_id': 221528}{'effort_instance_id': 33060}{'effort_instance_id': 221814}{'effort_instance_id': 221874}{'effort_instance_id': 221823}{'effort_instance_id': 221860}

###POST /entries/post_request/

Posts a new entry into the database. Application will send back a response if entry is flagged to be already in the database.

Valid parameters for POST request are: name,updated_on,updated_by,drupal_id,latitude,longitude, and all types of services go into an array called 'services'

Example of POST request paramaters:

"params": [
              {
                "name": "name",
                "value": "new_org"
              },
              {
                "name": "latitude",
                "value": "19.723866985609778"
              },
              {
                "name": "longitude",
                "value": "-72.18634030151367"
              },
              {
                "name": "services%5B%5D",
                "value": "Cardiovascular"
              },
              {
                "name": "services%5B%5D",
                "value": "Dental"
              },
              {
                "name": "services%5B%5D",
                "value": "Diabetes"
              },
              {
                "name": "services%5B%5D",
                "value": "Emergency"
              }
            ]

Example of response:

{
    "nearby_facilities": {
        "crs": {
            "type": "link",
            "properties": {
                "href": "http://spatialreference.org/ref/epsg/4326/",
                "type": "proj4"
            }
        },
        "type": "FeatureCollection",
        "features": [
            {
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        -72.18179999,
                        19.726299999
                    ]
                },
                "type": "Feature",
                "properties": {
                    "description": "",
                    "similarity": "nearby",
                    "default": null,
                    "date_end": null,
                    "date_start": null,
                    "longitude": "-72.18179999",
                    "drupal_id": 0,
                    "latitude": "19.726299999",
                    "provider_name": "CSL Madeline",
                    "service_provider": 7588,
                    "type": "CL",
                    "model": "entries.location_w_efforts_temp"
                },
                "id": 11893
            }
        ]
    }
}flagged



##Files:

The haiti_geospatial_data folder consists of shapefiles used for a web map.

The notes folder contains relevant notes, but nothing the code is dependent on.

The packer folder contains a json packer template that can be used to set-up an Ubuntu server AMI (AWS Machine Image) will all the required dependencies for hos-django

###hos2 folder:

- settings.py: Notice that GeoDjango django.contrib.gis app is included. Also 
that other databases can be connected to by uncommenting the appropriate code block. This 
makes it easy to switch from a local database to a shared database

- entries folder: The entries folder contains a data folder
that contains the CSVs that will be imported, all of the relevant python scripts to load data into PostGIS, 
and the templates folder that contains the templates for the views

###Python scripts(in entries folder):

- load_Service_Type_table.py must be run before the load data scripts. It populates the ServiceType table with all of the possible services, and this table needs to be populated so 
the necessary relations are created when the load data scripts are run.

- load data scripts: There are four individual scripts that load data from the four separate CSV files that are in the 
data folder (However there are 3 separate data sources). The scripts are load_data_hac.py, load_data_ong.py, load_data_mmex.py, and load_data_haiti_aid_map.py. Each of
these scripts loads that data into the appropriate table in the HOS database and creates the proper relations. A user can run these four scripts individually or run the load_all_data.py 
script to load all of the data into the geodatabase. 

- clear_all_data.py script clears all of the data in the database.

- service_type_dictionary.py is just a dictionary that the load data scripts import in order to related different entries that show up as services in the individual datasets so that they can be 
classified into one of the standard service types defined in the ServiceType table.

- load_geospatial_data.py loads the admin shapefiles found in the haiti_geospatial_data folder and imports them as polygons in the 
HOS1 geodatabase. This only needs to be run once after the database is created.

- The adm1_name_dict.py, adm2_name_dict.py, and adm3_name_dict.py are dictionaries so that the different entries in the individual datasets for admin areas can be 
classified to the admin names found in the respective haiti_admin tables.

- temp_loc_w_efforts_table.py produces a temporary table that has all of the location points and appends the 
start date, end date, and provider name.

- deduplicate_database.py: find possible effort instances that might be duplicates based on spatial proximity and string similarity.

###Dependencies

- pip install django-leaflet
- pip install django-geojson
- pip install requests
- pip install pyyaml 

###FAQ:

Why do I have trouble importing CSVs from my mac to Github?

On a Mac, Excel produces csv files with the wrong line endings, which causes problems for git (amongst other things).
see: http://nicercode.github.io/blog/2013-04-30-excel-and-line-endings/

For me, the issue importing CSV files on a Mac is that the importer doesn't support the default mac "record separator" (the line ending).
On a mac, the default line eding is CR (carriage return).
Unix line endings (LF: line feed) and Windows line endings (CRLF) are supported.
Changing the line ending of your csv file to eg. CR will make QGIS import the file just fine (I used TextWrangler).
(http://hub.qgis.org/issues/8421)


###Data Sources:

-HopeOneSource.org

Scraped Data:

MMEX:
www.mmex.org/missions?tid=1&tid_1=All&items_per_page=All&views_exposed_form_focused_field

HAC:
http://www.mspp.gouv.ht/cartographie/index.php#

ONG:
http://www.mspp.gouv.ht/cartographie/detail_ong.php?idInstitution=$popup

Haiti Aid Map:
haiti.ngoaidmap.org/

Geospatial Data: 

http://www.gvsu.edu/haitiwater/links-to-gis-data-for-haiti-9.htm




