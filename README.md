imdb-data-parser
================

Parses the IMDB dumps into CSV and Relational Database insert queries
Uses IMDB dumps from: http://www.imdb.com/interfaces

Requirements
================
Python 3.x

Configuring
================
All configuration data stays at `idp/settings.py.example`

You need to copy this file as `settings.py` and edit this file before running the project

    cd idp
    cp settings.py.example settings.py
    your_favourite_editor settings.py

Configuring DB
--------------

    sudo -u postgres createuser -D -A -P mynewuser
    sudo -u postgres createdb -O mynewuser mydatabase

Executing
=========

    ~/imdb-data-parser$ python3 imdbparser.py

You can use -h parameter to see list of optional arguments
