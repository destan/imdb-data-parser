#!/usr/bin/env python3

import sys
import argparse
import logging
import logging.config
from idp.parser.parsinghelper import ParsingHelper
from idp.settings import *

# check python version
if sys.version_info.major != 3:
    sys.exit("Error: wrong version! You need to install python3 to run this application properly.")

logging.config.fileConfig("logging.conf")

parser = argparse.ArgumentParser(description="an IMDB data parser")
parser.add_argument('-m', '--mode', help='Parsing mode, defines output of parsing process. Default: CSV', choices=['TSV', 'SQL', 'DB'])
parser.add_argument('-s', '--source_dir', help='source directory of interface lists')
parser.add_argument('-d', '--destination_dir', help='destination directory for outputs')
parser.add_argument('-u', '--update_lists', action='store_true', help='downloads lists from server')

args = parser.parse_args()
logging.info("mode:%s", args.mode)
logging.info("source_dir:%s", args.source_dir)
logging.info("destination_dir:%s", args.destination_dir)
logging.info("update_lists:%s", args.update_lists)

if args.update_lists:
    from idp.utils import listdownloader
    logging.info("Downloading IMDB dumps, this may take a while depending on your connection speed")
    listdownloader.download()

logging.info("Parsing, please wait. This may take very long time...")

# preparing preferences map
if args.mode:
    mode = args.mode
else: #default
    mode = "TSV"

if args.source_dir:
    sourcePath = args.source_dir
else:
    sourcePath = SOURCE_PATH

if args.destination_dir:
    destinationPath = args.source_dir
else:
    destinationPath = DESTINATION_PATH

preferencesMap = {
    "mode":mode, 
    "destinationDir": args.destination_dir,
    "sourcePath": sourcePath,
    "destinationPath": destinationPath
}

ParsingHelper.parse_all(preferencesMap)

print ("All done, enjoy ;)")