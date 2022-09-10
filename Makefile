
install:
		poetry install

lint:
		poetry run flake8 task_manager

test:
		poetry run python3 manage.py test chgk/tests

startproject:
		poetry run django-admin startproject chgk .

runserver:
		poetry run python manage.py runserver

gunicorn:
		export DJANGO_SETTINGS_MODULE=chgk.settings
		poetry run gunicorn chgk.wsgi

requirements:
		poetry export --without-hashes -f requirements.txt -o requirements.txt

makemigrations:
		 poetry run python manage.py makemigrations

migrate:
		 poetry run python manage.py migrate

herokumigrate:
		heroku run python manage.py migrate

collectstatic:
		poetry run python manage.py collectstatic --noinput