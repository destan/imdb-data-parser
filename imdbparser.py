#!/usr/bin/env python3

import sys
import argparse
from idp.parser.parsinghelper import ParsingHelper
from idp import settings

# check python version
if sys.version_info.major != 3:
    sys.exit("Error: wrong version! You need to install python3 to run this application properly.")

parser = argparse.ArgumentParser(description="an IMDB data parser")
parser.add_argument('-m', '--mode', help='Parsing mode, defines output of parsing process. Default: CSV', choices=['TSV', 'SQL', 'DB'])
parser.add_argument('-s', '--source_dir', help='source directory of interface lists', required=True)
parser.add_argument('-d', '--destination_dir', help='destination directory for outputs', required=True)
parser.add_argument('-u', '--update_lists', action='store_true', help='downloads lists from server')

args = parser.parse_args()
print("mode:", args.mode)
print("source_dir:", args.source_dir)
print("destination_dir:", args.destination_dir)
print("update_lists:", args.update_lists)

if args.update_lists:
    from idp.utils import listdownloader
    print("Downloading IMDB dumps, this may take a while depending on your connection speed")
    listdownloader.download()

print("Parsing, please wait. This may take very long time...")

# preparing preferences map
if(args.mode is not None):
    mode = args.mode
else: #default
    mode = "TSV"

preferencesMap = {
    "mode":mode, 
    "destinationDir": args.destination_dir,
    "sourcePath": args.source_dir,
    "destinationPath": args.destination_dir
}

ParsingHelper.parse_all(preferencesMap)

print ("All done, enjoy ;)")