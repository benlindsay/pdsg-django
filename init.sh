#!/bin/bash
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Ben Lindsay <benjlindsay@gmail.com>

echo "Running makemigrations on account app:"
python manage.py makemigrations account
echo "Running makemigrations on events app:"
python manage.py makemigrations events
echo "Running migrate:"
python manage.py migrate
echo "Populating school choices for profiles:"
python manage.py populate_schools
echo "Populating degree choices for profiles:"
python manage.py populate_degrees
echo "Creating superuser account:"
python manage.py createsuperuser
