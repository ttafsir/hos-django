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


###GET /entries/'pk'/results/

Returns other what services the requested health facility provides. Insert the EffortInstance ID for 'pk'

Example:

http://example.org/entries/11887/results/

response:

["General consultation", "Pediatrics", "Malaria", "Emergency", "Physical therapy", "Vaccination (PEV)", "Dental", "Pharmacy", "Operating room", "Obstetric care", "Palliative care", "Hypertension", "Laboratory", "Cardiovascular", "Psychology service", "ObGyn", "Diabetes"]


###GET /entries/shared_servicetype/

Returns other health facilities that offer the same type of services.

Example:

http://example.org/entries/shared_servicetype/?id=33149

response:

{'effort_instance_id': 33009}{'effort_instance_id': 33089}{'effort_instance_id': 33108}{'effort_instance_id': 111286}{'effort_instance_id': 33091}{'effort_instance_id': 33101}{'effort_instance_id': 33131}{'effort_instance_id': 111040}{'effort_instance_id': 111037}{'effort_instance_id': 33018}{'effort_instance_id': 33044}{'effort_instance_id': 33107}{'effort_instance_id': 33138}{'effort_instance_id': 111171}{'effort_instance_id': 11971}{'effort_instance_id': 33032}{'effort_instance_id': 33056}{'effort_instance_id': 11870}{'effort_instance_id': 111101}{'effort_instance_id': 111051}{'effort_instance_id': 111214}{'effort_instance_id': 111032}{'effort_instance_id': 111202}{'effort_instance_id': 33092}{'effort_instance_id': 33132}{'effort_instance_id': 111319}{'effort_instance_id': 33146}{'effort_instance_id': 111318}{'effort_instance_id': 33122}{'effort_instance_id': 33129}{'effort_instance_id': 33104}{'effort_instance_id': 111559}{'effort_instance_id': 33105}{'effort_instance_id': 33149}{'effort_instance_id': 111339}{'effort_instance_id': 33121}{'effort_instance_id': 33082}{'effort_instance_id': 11792}{'effort_instance_id': 11847}{'effort_instance_id': 33148}{'effort_instance_id': 33038}{'effort_instance_id': 111382}{'effort_instance_id': 11936}{'effort_instance_id': 111485}{'effort_instance_id': 11820}{'effort_instance_id': 33133}{'effort_instance_id': 33076}{'effort_instance_id': 33021}{'effort_instance_id': 33117}{'effort_instance_id': 33063}{'effort_instance_id': 33042}{'effort_instance_id': 111030}{'effort_instance_id': 111189}{'effort_instance_id': 33036}{'effort_instance_id': 111077}{'effort_instance_id': 11906}{'effort_instance_id': 111431}{'effort_instance_id': 11812}{'effort_instance_id': 33094}{'effort_instance_id': 33039}{'effort_instance_id': 33120}{'effort_instance_id': 33050}{'effort_instance_id': 111278}{'effort_instance_id': 111396}{'effort_instance_id': 33001}{'effort_instance_id': 111239}{'effort_instance_id': 111107}{'effort_instance_id': 111082}{'effort_instance_id': 11903}{'effort_instance_id': 33028}{'effort_instance_id': 111364}{'effort_instance_id': 33100}{'effort_instance_id': 11930}{'effort_instance_id': 11995}{'effort_instance_id': 33139}{'effort_instance_id': 111235}{'effort_instance_id': 33037}{'effort_instance_id': 33084}{'effort_instance_id': 111172}{'effort_instance_id': 33031}{'effort_instance_id': 33143}{'effort_instance_id': 111093}{'effort_instance_id': 33040}{'effort_instance_id': 33136}{'effort_instance_id': 111131}{'effort_instance_id': 33002}{'effort_instance_id': 33109}{'effort_instance_id': 33128}{'effort_instance_id': 11795}{'effort_instance_id': 111250}{'effort_instance_id': 33060}{'effort_instance_id': 33112}{'effort_instance_id': 33051}{'effort_instance_id': 111144}{'effort_instance_id': 111563}{'effort_instance_id': 111450}{'effort_instance_id': 33007}{'effort_instance_id': 33145}{'effort_instance_id': 11885}{'effort_instance_id': 33086}

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
}



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

###Python scripts (in entries folder):

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




