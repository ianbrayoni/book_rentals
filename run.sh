#!/bin/sh

# attempt to run migrations
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate

# collect static files
pipenv run python manage.py collectstatic

# start app
# pipenv run python manage.py runserver 0.0.0.0:5000
pipenv run gunicorn --workers=2 --bind=0.0.0.0:5000 --log-level=info book_rentals.wsgi