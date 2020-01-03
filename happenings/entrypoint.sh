#!/bin/sh

python manage.py migrate
python manage.py collectstatic --no-input --clear

# Make an admin user for devs for quicker setup
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('dev', 'dev@example.com', 'dev')"

 exec "$@"
