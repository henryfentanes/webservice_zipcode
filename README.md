# webservice_zipcode
An api to get and store information from the zip_code using third party service <a href="http://postmon.com.br" target="_blank">Postmon</a>

### How to Play:
webservice_zipcode api is a standard django project. To work with it should be as easy as
- cloning the project;
 - git clone https://github.com/henryfentanes/webservice_zipcode.git
- making a <a href="http://virtualenv.readthedocs.org/en/latest/userguide.html" target="_blank">virtualenv</a> and activating to prevent messing with your system's python env;
 - virtualenv webservice_venv and then source webservice_venv/bin/activate (on unix)
 - virtualenv webservice_venv and then webservice_venv/Scripts/activate (on windows)
- use pip to install the project requirements;
 - pip install -r requirements.txt
- create the database with django's migrate;
 - python manage.py migrate
- put the server up and running.
 - python manage.py runserver

Although, if you're running on a linux or a mac, simply running the configure.sh and then run.sh should suffice.
> configure.sh should create the virtualenv, activate it, install the requirements, migrate the database and collect static files;
> run.sh should run put the server running with gunicorn


### Or You can just use it online
##### Include
*curl --data "zip_code=14020260" https://api-cep-henryfentanes.herokuapp.com/zipcode/*

##### Exclude
*curl -X DELETE https://api-cep-henryfentanes.herokuapp.com/zipcode/14020260/*

##### Detail
*curl https://api-cep-henryfentanes.herokuapp.com/zipcode/14020260/*

##### List
*curl https://api-cep-henryfentanes.herokuapp.com/zipcode/?limit=xxx*
> You may omit ?limit=xxx to list All the records

Records are logged every time a zip-code is created, deleted or detailed.
##### Log list for specific zipcode
*curl https://api-cep-henryfentanes.herokuapp.com/log/14020260/*
