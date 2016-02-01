#!/bin/bash

#########################################################
######## CONFIGURANDO AMBIENTE CODING CHALLENGE #########
#########################################################

#
# Get enviroment (linux or mac)
#

OS=`uname`


#
# Set Dirs
#

CURRENTDIR=`pwd`;
PROJECTNAME=`basename $CURRENTDIR`;
VIRTUALENVDIR=$CURRENTDIR/venv;

#
# Create virtualenv in case it doesn't exist
#

if [ ! -d $VIRTUALENVDIR ]; then
    if [ -x virtualenv ]; then
        virtualenv $VIRTUALENVDIR;
    else
        echo "python-virtualenv não encontrada, é necessário instala-la";
        if [ $OS == "Linux" ]; then
            sudo apt-get install python-virtualenv -y;
            virtualenv $VIRTUALENVDIR;
        elif [ $OS == "Darwin" ]; then
            sudo easy_install pip;
            sudo pip install virtualenv;
            virtualenv $VIRTUALENVDIR;
        else
            exit 1;
        fi
    fi
fi


#
# Activate virtualenv
#

source $VIRTUALENVDIR/bin/activate;


#
# Install requirements
#
pip install -r requirements.txt;

#
# Migrate Database
#

python manage.py migrate;

#
# Colect static files
#
python manage.py collectstatic --noinput