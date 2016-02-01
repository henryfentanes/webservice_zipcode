#!/bin/bash

#########################################################
###### DISPONIBILIZANDO O FUNCIONAMENTO DO SISTEMA ######
#########################################################

#
# Determinando ambiente (linux ou mac)
#

OS=`uname`


#
# Setando os Diretorios
#

CURRENTDIR=`pwd`;
PROJECTNAME=`basename $CURRENTDIR`;
VIRTUALENVDIR=$CURRENTDIR/venv;

#
# Criar virtualenv caso ela não exista
#

if [ ! -d $VIRTUALENVDIR ]; then
    echo "Please run configure.sh first"
    if [ -x nginx ]; then
        sudo service nginx start;
    else
        echo "Nginx not found, it is a requirement";
        if [ $OS == "Linux" ]; then
            sudo apt-get install nginx
        else
            exit 1;
        fi
    fi
fi

#
# Ativar virtualenv
#

cd $VIRTUALENVDIR;
source bin/activate;
cd $PROJECTNAME


#
# Informar o usuário de como acessar o sistema
#
echo "########################################################################"
echo "####You can now go to your browser and access http://localhost:8080#####"
echo "########################################################################"

#
# Levantando o servidor
#
if [ $OS == "Linux" ]; then
    gunicorn --bind 0.0.0.0:8080 webservice_cep.wsgi
elif [ $OS == "Darwin" ]; then
    if [ -x nginx ]; then
        gunicorn --bind 0.0.0.0:8080 webservice_cep.wsgi
    else
        python manage.py runserver 0.0.0.0:8080
    fi
fi