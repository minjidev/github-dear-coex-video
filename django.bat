@echo off

docker-compose -f local.yml run --rm django python manage.py makemigrations

docker-compose -f local.yml run --rm django python manage.py migrate 

docker-compose -f local.yml up  