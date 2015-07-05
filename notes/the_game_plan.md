GamePlan
===========

Next Goals:

- Integration with main Drupal site
	-we need to work on the import from the HOS side:
		1)Location in Lat and Lon
		2)Name of Org
		3)Services provided(if available)

- Write Ansible scripts for server deployment

- when the user makes a decision and re-submits the form, there can be a flag variable that specifies whether 
the new POST request is creating a new org or associating with an existing one.(This part isn't implemented yet)

Sidegoal:

- make web-map

Changes to HOS DB on 5 Oct 2014:

-added provider_name_fr and provider_name_cr provider names to ServiceProvider table
-added updated_on,updated_by,description, and default (boolean) fields to EffortInstance table
-added to Location table save function to automatically create a row in the Location_w_efforts table when a Location is saved
-added a Common_EffortInstance_Info Abstraction table
-renamed EffortInstanceServices table to EffortInstanceService

**need to add django-geodjango and possibly django-leaflet into dependencies?

1 Dec 2014:

-you can check the Django version by typing the following into the command line: python -c "import django; print(django.get_version())"

-Django is upgraded to 1.71
-had some issues upgrading (see Toms_Installing_Django notes)

got this error after this command(python load_servicetype_table.py):
 raise AppRegistryNotReady("Models aren't loaded yet.")
django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.

so did this:
-added the following 2 lines to top of load_servicetype_table.py (**don't think it was necessary though**) 

import django
django.setup()

got this error:
django.core.exceptions.ImproperlyConfigured: Requested setting LOGGING_CONFIG, but settings are not configured. 
You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.

so ran this:
Tom-Gertins-MacBook-Pro:entries thomasgertin1$ export DJANGO_SETTINGS_MODULE=hos2.settings
and got this error: 
ImportError: Could not import settings 'hos2.settings' (Is it on sys.path? Is there an import error in the settings file?): No module named hos2.settings

so exported the following into my Python path:
http://stackoverflow.com/questions/20270297/consistently-getting-importerror-could-not-import-settings-myapp-settings-err
Tom-Gertins-MacBook-Pro:entries thomasgertin1$ export PYTHONPATH=/Users/thomasgertin3/repos/hos-django/:$PYTHONPATH

and I was finally able to run:

Tom-Gertins-MacBook-Pro:entries thomasgertin1$ python load_servicetype_table.py

14 Feb 2015:

-added requests module (sudo pip install requests)
