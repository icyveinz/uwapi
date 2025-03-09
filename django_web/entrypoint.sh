#!/bin/bash

# Wait until PostgreSQL is ready
until pg_isready -h db -p 5432 -U user -d applications_db; do
  echo "Waiting for PostgreSQL to be ready..."
  sleep 2
done

echo "PostgreSQL is ready. Running migrations..."

# Run migrations
python manage.py migrate --noinput

# Collect static files (optional if needed)
python manage.py collectstatic --noinput

echo "Starting the Django application..."

# Start the application
exec gunicorn --bind 0.0.0.0:8001 django_web.wsgi:application