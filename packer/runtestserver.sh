#!/bin/bash
#runserver script

echo "Starting Django development server"
#activates virtualenv
source /home/ubuntu/py27env/bin/activate
cd /home/ubuntu/hos-django
python manage.py runserver 172.31.59.160:80