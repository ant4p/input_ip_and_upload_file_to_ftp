#!/bin/sh


until
    python manage.py makemigrations
    sleep 5
    python manage.py migrate

do
  echo "...prepare_database..."
  sleep 20

done

sleep 5

gunicorn --bind 0.0.0.0:8000 app.wsgi