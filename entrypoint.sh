#!/bin/sh

echo "🔁 Waiting for PostgreSQL to be ready..."
/app/wait-for-postgres.sh

echo "📦 Running migrations..."
python manage.py migrate

echo "📂 Collecting static files..."
python manage.py collectstatic --noinput

# ✅ เพิ่มการสร้าง superuser
python manage.py shell < /app/create_superuser.py

echo "🚀 Starting Gunicorn server..."
exec gunicorn rimesproject.wsgi:application --bind 0.0.0.0:8000