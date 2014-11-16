GamePlan
===========

current Goal: De-Duplication

In order to identify duplicates from the combined dataset.

Step 1:

- Thread 1: Finish tying each dataset to a location. For the datasets that don't have lat-lon, match them to the appropriate admin zone
	-completed on 8 June by Tom

- Thread 2: Research the best way to find compare and find similar strings. We want something more advanced than a 'like' function
is there something like a python library that does this? nltk (natural language toolkit) 
	-we ended up using the python difflib for this

Step 2:

- Thread 1: create a psuedo-code version of the de-duplicator. It should look similarities from organization names as well as locations,
maybe times as well? 
	-completed

Next Goals:

- Documentation: progress made
- Testing: assign to Kat and Tafsir
- manually get rid of duplicates (procedure for database versions): maybe dumpdata/loaddata Django commands?
	-http://stackoverflow.com/questions/21049330/how-to-backup-a-django-db
- create dev and production github repos: created a master and develop branch
	-complete
	
- Integration with main Drupal site
	-we need to work on the import from the HOS side:
		1)Location in Lat and Lon
		2)Name of Org (Also French and Creole versions if available)
		3)Services provided(if available)

when the user makes a decision and resubmits the form, their can be a flag variable that specifies whether 
the new POST request is creating a new org or associating with an existing one.(This part isn't implemented yet)

Sidegoal:

- make web-map
- getting people to connect to AWS instances


Other, to-do list:

-finish writing temporary table to display most important information in QGIS
	-complete

-start looking into WebGIS

-Start thinking about moving to a different branching Git model(dev and production versions)
	-check out: http://nvie.com/posts/a-successful-git-branching-model/

-update Database diagram: check

Changes to HOS DB on 5 Oct 2014:

-added provider_name_fr and provider_name_cr provider names to ServiceProvider table
-added updated_on,updated_by,description, and default (boolean) fields to EffortInstance table
-added to Location table save function to automatically create a row in the Location_w_efforts table when a Location is saved
-added a Common_EffortInstance_Info Abstraction table
-renamed EffortInstanceServices table to EffortInstanceService

**need to add django-geodjango and possibly django-leaflet into dependencies?


