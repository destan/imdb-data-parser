#!/usr/bin/env python3

import sys
import argparse
from idp.parser.moviesparser import MoviesParser

# check python version
if sys.version_info.major != 3:
    sys.exit("Error: wrong version! You need to install python3 to run this application properly.")

parser = argparse.ArgumentParser(description="an IMDB data parser")
parser.add_argument('-t', '--type', help='type of the output files. default: CSV', choices=['TSV', 'SQL', 'DB'])
parser.add_argument('-s', '--source_dir', help='source directory of interface lists')
parser.add_argument('-d', '--destination_dir', help='destination directory for outputs')
parser.add_argument('-u', '--update_lists', action='store_true', help='downloads lists from server')

args = parser.parse_args()
print("type:", args.type)
print("source_dir:", args.source_dir)
print("destination_dir:", args.destination_dir)
print("update_lists:", args.update_lists)

if args.update_lists:
    from idp.utils import listdownloader
    listdownloader.download()

print("Parsing, please wait. This may take very long time...")

preferencesMap = {"type":args.type.lower(), "destinationDir": args.destination_dir}

movieParser = MoviesParser()
movieParser.startProcessing(preferencesMap)