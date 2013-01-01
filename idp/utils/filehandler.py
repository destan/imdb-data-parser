import gzip
import os.path
from ..settings import *
import logging

def get_full_path(filename, isCompressed = False):
    """
    constructs a full path for a dump file in the SOURCE_PATH
    filename should be without '.list'
    """
    if(isCompressed):
        return os.path.join(SOURCE_PATH, filename) + ".gz"
    else:
        return os.path.join(SOURCE_PATH, filename)

def get_full_path_for_tsv(filename):
    return get_full_path(filename) + ".tsv"

def get_decompressed_file_name(fullpath):
    return fullpath[:-3]

def extract(fullpath):
    try:
        logging.info('started to extract list: %s', fullpath)
        with gzip.open(fullpath, 'rb') as f:
            file_content = f.read()
        listfile = open(get_decompressed_file_name(fullpath), 'wb')
        listfile.write(file_content)
        listfile.close()
        logging.info(fullpath + ' list extracted successfully')
    except Exception as e:
        logging.error('error when extracting list: ' + fullpath + "\n\t" + str(e))
        return 1
    return 0

def openfile(fullFilePath):

    logging.info("Trying to find file: %s", fullFilePath)
    if os.path.isfile(fullFilePath):
        logging.info("File found: %s", fullFilePath)
        return open(fullFilePath, "r", encoding='iso-8859-1')

    logging.error("File cannot be found: %s", fullFilePath)

#
#this part removed until python 3.3 becomes available for ubuntu LTS and debian
#
#   print("Trying to find file:", fullFilePath)
#   if os.path.isfile(fullFilePath):
#       print("File found:", fullFilePath)
#       return gzip.open(fullFilePath, 'rt')
#   print("File cannot be found:", fullFilePath)

    logging.info("Trying to find file: %s", fullFilePath + ".gz")
    if os.path.isfile(fullFilePath + ".gz"):
        logging.info("File found: %s", fullFilePath + ".gz")
        if extract(fullFilePath + ".gz") == 0:
            return open(fullFilePath, "r", encoding='iso-8859-1')
        else:
            raise RuntimeError("Unknown error occured")
    logging.error("File cannot be found: %s", fullFilePath + ".gz")

    raise RuntimeError("FileNotFoundError: " + fullFilePath)