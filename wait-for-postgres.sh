#!/bin/sh

# รอ PostgreSQL ให้พร้อม
while ! nc -z "$DB_HOST" "$DB_PORT"; do
  echo "Waiting for PostgreSQL at $DB_HOST:$DB_PORT..."
  sleep 1
done

echo "✅ PostgreSQL is available!"