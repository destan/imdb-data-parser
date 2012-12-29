import os
import sys
import getopt

# imdbParser -s /source/dir/ -d /destination/dir/

HELP = "Command must be: imdbParser -s /source/dir/ -d /destination/dir/"

IMDB_SOURCE_DIR = None
IMDB_DESTINATION_DIR = None

try:
	optlist = getopt.getopt(sys.argv[1:], 's:d')

except getopt.error as err:
	print('Troubles with arguments.')
	print(HELP)
	sys.exit(2)
