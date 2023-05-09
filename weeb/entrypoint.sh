#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for PostgreSQL..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
        sleep 1
    done

    echo "PostgreSQL started"
fi

python manage.py migrate

exec "$@"
