# Django Graphql
Basic CRUD API with django and Graphene


![python version](https://img.shields.io/badge/python-3.10.10-brightgreen)
![django version](https://img.shields.io/badge/django-4.2.3-brightgreen)

## Tech stack
* django
* postgres
* graphene

## Clone
```
git clone git@github.com:Kriz1618/django-graphene.git
```

## Create and activate a virtual environment
* `python -m venv venv`
* `source venv/bin/activate`

## Install modules
```
python -m pip install -r requirements.txt
```

## Start
```
python manage.py runserver
```

## Run Tests
```
python manage.py test
```

## Format Code
```
autopep8 -i */*.py
black .
```

## Clear Docker Volumes
```
docker system prune -af --volumes
```


## Steps
* Create folder `mkdir django-graphql && cd django-graphql`
* Create virtual environment `python -m venv venv`
* Install dependencies `pip install Django pipreqs`
* Create project `django-admin startproject core .`
* Create an app `python manage.py startapp articles`
* Register app in the `settings.py` filed at `INSTALLED_APPS`
* Create a super user `python manage.py createsuperuser --email admin@example.com --username admin`
* Define the model in the file `articles/models.py`
* Create a new migration `python manage.py makemigrations articles`
* Execute migration `python manage.py migrate articles`
* Define viewSets in the file `articles/views.py`
* Freeze modules in the requirements file `pipreqs --force`
* List endpoints `python manage.py show_urls`


## Dockerization
* Create the [Dockerfile](https://docs.docker.com/engine/reference/builder/) file
* Build the image `docker build -t image-tag .`
* Run a container base on the created image `docker run -p 8000:8000 image-tag`
* Create the [docker-compose.yml](https://docs.docker.com/compose/compose-file/compose-file-v3/) file
* Create and run a container `docker-compose up -d`


## Running with uWSGI
* Replace the CMD command in the Dockerfile to `CMD ["uwsgi", "--ini", "uwsgi.ini"]`
* Add the uWSGI module in the requirements file `uWSGI==2.0.23`
* Create the `uwsgi.ini` configuration file


## Add a local custom host to test ALLOWED_HOST configuration
* open the file `/Windows/System32/drivers/etc/hosts`
* Set the following configuration
```
127.0.0.1 example.test
::1 example.test localhost
```
