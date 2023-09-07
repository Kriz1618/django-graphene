# Django Graphql
Basic CRUD API with django and Graphene

## Required Tools
* Python
*  Django

## Clone
```
git clone git@github.com:Kriz1618/django-graphene.git
```

## Create and activate a virtual environment
* `python -m venv venv`
* `source env/bin/activate`

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
