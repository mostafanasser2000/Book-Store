#!/usr/bin/bash
docker compose exec web python manage.py makemigrations $1