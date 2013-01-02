from ..settings import *
from ftplib import FTP
import gzip
from .filehandler import *
import logging

def download():
    logging.info("lists will downloaded from server:" + INTERFACES_SERVER)

    ftp = FTP(INTERFACES_SERVER)
    ftp.login()
    download_count = 0
    for list in LISTS:
        try:
            logging.info("started to download list:" + list)
            r = ftp.retrbinary('RETR '+INTERFACES_DIRECTORY+list+'.list.gz',
                open(SOURCE_PATH+list+'.list.gz', 'wb').write)
            logging.info(list + "list downloaded successfully")
            download_count = download_count+1
            extract(get_full_path(list+".list", True))
        except Exception as e:
            print("ERROR: there is a problem when downloading list " + list + "\n\t" + str(e))
    logging.info(str(download_count) + " lists are downloaded")
    ftp.quit()