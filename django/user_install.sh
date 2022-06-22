#!/bin/bash

python3 -m venv /home/toto/django/SAE24/.venv
source /home/toto/django/SAE24/.venv/bin/activate
pip3 install django django-admin mysqlclient gunicorn crispy-bootstrap5 Pillow reportlab

python3 /home/toto/django/SAE24/manage.py makemigration
python3 /home/toto/django/SAE24/manage.py migrate
python3 /home/toto/django/SAE24/manage.py collectstatic

#python3 /home/toto/django/manage.py runserver
#/home/toto/django/.venv/bin/gunicorn --bind 0.0.0.0:8000 SAE23.wsgi
