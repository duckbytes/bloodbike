#!/bin/bash

read -s -p "Please set a password for the admin user: " pswd

if ! systemctl list-units | grep -q -i postgres; then
    echo "Please install and start the postgresql database server (sudo systemctl start postgresql)"
    exit
else
    echo "Postgres found. Creating database. You may need to provide your sudo password."
fi

sudo su - postgres -c 'psql -c "create database bloodbike_dev"'

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

cp api_jwt.py venv/lib/python3.*/site-packages/jwt

flask db upgrade

python setup.py $pswd

echo "Completed setup"