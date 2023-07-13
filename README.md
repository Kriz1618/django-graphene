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
* Create project `django-admin startproject core .`
* Create an app `python manage.py startapp articles`
* Register app in the `settings.py` filed at `INSTALLED_APPS`
* Create a super user `python manage.py createsuperuser --email admin@example.com --username admin`
* Define the model in the file `articles/models.py`
* Create a new migration `python manage.py makemigrations articles`
* Excecute migration `python manage.py migrate articles`
* Define viewSets in the file `articles/views.py`
* Freeze modules in the requirements file `pip freeze >> requirements.txt`
* List endpoints `python manage.py show_urls`
