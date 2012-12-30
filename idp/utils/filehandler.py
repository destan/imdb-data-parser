import gzip
import os.path
from ..settings import *

def full(filename):
    try:
        print('started to extract list: ', filename)
        with gzip.open(get_full_path(filename) + '.list.gz', 'rb') as f:
            file_content = f.read()
        listfile = open(get_full_path(filename) +'.list', 'wb')
        listfile.write(file_content)
        listfile.close()
        print(filename, 'list extracted successfully')
    except:
        print('error when extracting list:'. filename)
        return 1
    return 0

def get_full_path(filename, isCompressed = False):
    """
    constructs a full path for a dump file in the SOURCE_PATH
    filename should be without '.list'
    """
    if(isCompressed):
        return SOURCE_PATH + filename + ".gz"
    else:
        return SOURCE_PATH + filename

def get_full_path_for_tsv(filename):
    return get_full_path(filename) + ".tsv"

def openfile(fullFilePath):

    print("Trying to find file:", fullFilePath)
    if os.path.isfile(fullFilePath):
        print("File found:", fullFilePath)
        return open(fullFilePath, "r", encoding='iso-8859-1')

    print("File cannot be found:", fullFilePath)

#
#this part removed until python 3.3 becomes available for ubuntu LTS and debian
#
#   print("Trying to find file:", fullFilePath)
#   if os.path.isfile(fullFilePath):
#       print("File found:", fullFilePath)
#       return gzip.open(fullFilePath, 'rt')
#   print("File cannot be found:", fullFilePath)

    print("Trying to find file:", fullFilePath + ".gz")
    if os.path.isfile(fullFilePath + ".gz"):
        print("File found:", fullFilePath + ".gz")
        if extract(inputDir, inputFileName) == 0:
            return open(fullFilePath, "r", encoding='iso-8859-1')
        else:
            raise RuntimeError("Unknown error occured")
    print("File cannot be found:", fullFilePath + ".gz")

    raise BaseException("FileNotFoundError")