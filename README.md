# IoT-Project-Smart-Fan

## Group Members/Collaborators:

1. Ashwin Shanmugam - 100700236
2. Esam Uddin - 100711116
3. Mihirkumar Patel - 100702168

## Run App 

- https://projectgroup11.ml:1880/ui

Installation (assignment 2)

```
pip install django
```
```
pip install djangorestframework
```

Run App

```
python manage.py runserver
```

## Demo

![Alt text](/App.PNG?raw=true "demo")

### Table of Contents:

#### - assignment2 

The main src folder which containts both the project folder and the app folder. The folder also includes a file called manage.py which is a command-line utility that lets us interact with this project. (ex. running the app)

#### - assignment2/assignment2 

The project folder that contains a collection of settings including database configuration, Django-specific options, and application-specific settings. The folders included in the project folder are the following:

```
assignment 2/
    __init__.py
    settings.py
    urls.py
    asgi.py
    wsgi.py
```
#### - assignment2/smartapp

The app folder was created to run the web application for our project and display the database records using rest services. The folders included in the app folder are the following:


```
smartfan/
    __init__.py
    admin.py
    apps.py
    templates/smartfan
         home.html
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
    serializers.py
    urls.py
```




