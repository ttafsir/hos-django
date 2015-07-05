#!/bin/bash
#runserver script

echo "Starting Gunicorn Server"
source /home/ubuntu/py27env/bin/activate
cd /home/ubuntu/hos-django/hos2
gunicorn wsgi:application --bind 127.0.0.1:8001