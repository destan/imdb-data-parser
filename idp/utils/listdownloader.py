from ..settings import *
from ftplib import FTP
import gzip

def download():
    print("lists will downloaded from server:", INTERFACES_SERVER)

    ftp = FTP(INTERFACES_SERVER)
    ftp.login()
    download_count = 0
    for list in LISTS:
        try:
            print("started to download list:" + list)
            r = ftp.retrbinary('RETR pub/misc/movies/database/'+list+'.list.gz',
                open(INPUT_DIRECTORY + list + '.list.gz', 'wb').write)
            print(list + "list downloaded successfully")
            download_count = download_count+1
            extract(list)
        except:
            print("ERROR: there is a problem when downloading list " + list)

    print(download_count, " lists are downloaded")
    ftp.quit()

def extract(filename):
    try:
        print('started to extract list: ', filename)
        with gzip.open(INPUT_DIRECTORY + filename + '.list.gz', 'rb') as f:
            file_content = f.read()
        listfile = open(INPUT_DIRECTORY + filename +'.list', 'wb')
        listfile.write(file_content)
        listfile.close()
        print(filename, 'list extracted successfully')
    except:
        print('error when extracting list:'. filename)
        return 1
    return 0



