web: python manage.py runserver 0.0.0.0:$PORT
release: python manage.py migrate
web:gunicorn wedding_project.wsgi --log-file -