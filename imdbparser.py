#!/usr/bin/env python3

import sys
import argparse
<<<<<<< Updated upstream
from idp.parser.moviesparser import MoviesParser
=======
from idp.parser import moviesparser
>>>>>>> Stashed changes

# check python version
if sys.version_info.major != 3:
    sys.exit("Error: wrong version! You need to install python3 to run this application properly.")

parser = argparse.ArgumentParser(description="an IMDB data parser")
parser.add_argument('-t', '--type', help='type of the output files. default: CSV', choices=['TSV', 'SQL', 'DB'])
parser.add_argument('-s', '--source_dir', help='source directory of interface lists')
parser.add_argument('-d', '--destination_dir', help='destination directory for outputs')

args = parser.parse_args()
print("type:", args.type)
print("source_dir:", args.source_dir)
print("destination_dir:", args.destination_dir)
<<<<<<< Updated upstream
print("Parsing, please wait. This may take very long time...")

preferencesMap = {"type":args.type.lower(), "destinationDir": args.destination_dir}

movieParser = MoviesParser()
movieParser.startProcessing(preferencesMap)
=======
print(args)

moviesparser.parseLists()
>>>>>>> Stashed changes
