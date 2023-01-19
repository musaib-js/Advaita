web: gunicorn advaita.wsgi --log-file -
web: python manage.py collectstatic --no-input; gunicorn advaita.wsgi --log-file - --log-level debug