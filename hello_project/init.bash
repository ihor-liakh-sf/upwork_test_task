#!/bin/sh
cd hello_project
python manage.py migrate
python manage.py loaddata hello_world
python manage.py runserver 0.0.0.0:8000
