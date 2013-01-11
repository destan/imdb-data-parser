imdb-data-parser
================

    This repo is *obsolete* now, active development is ongoing in https://github.com/dedeler/imdb-data-parser

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

Execute
-------

    ~/imdb-data-parser$ python3 imdbparser.py

You can use -h parameter to see list of optional arguments
