#!/bin/sh

echo "entrypoint pwd:"
pwd
echo "entrypoint ls:"
ls
python manage.py migrate
python manage.py collectstatic --no-input --clear

echo "entrypoint end"

exec "$@"