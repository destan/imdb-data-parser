from ..settings import *
from ftplib import FTP
import gzip
from filehandler import *

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
