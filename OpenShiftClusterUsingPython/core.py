import argparse
import os
import time
import configparser
import logging
from client import OCApiCall

LOG_FORMAT = "%(levelname)s %(asctime)s -%(message)s"
# logging configuration
logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'random.log'), level=logging.DEBUG,
                    format=LOG_FORMAT, filemode='a')
logger = logging.getLogger()
print(f'Logger Level - {logger.level}')
# logger level will be in Numeric.


def readconfig():
    config = configparser.ConfigParser()
    # print(f'current dir: {os.getcwd()}')
    # file = os.path.join(os.getcwd(), "config.ini")
    file = config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
    # print(f'File Path: {file}')
    lst = {}
    try:
        with open(file[0], 'r') as configfile:
            config.read(configfile)
            apikey = config['OPENSHIFT']['APIKEY']
            url = config['OPENSHIFT']['HOST']
            logger.debug(f'URL Value: {url}')
            lst["apikey"] = apikey
            lst["url"] = url
            return lst
            # In Python, comma-separated values are considered tuples without parentheses,
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        logger.info("File has been read")


def banner(mess, border='-'):
    line = border * len(mess)
    print(line)
    print(mess)
    print(line)


def main():
    """
    The main function will Pre-process args
    """
    # banner("Execution Started at " + time.ctime(), "*")
    banner(' '.join(["Started", time.ctime()]), "*")
    x = readconfig()
    _apikey = x["apikey"]
    _url = x["url"]
    _namespace = input("Enter NameSpace: ")
    z = OCApiCall(_apikey, _url, _namespace)
    z.kubecall()
    banner("Execution Fished at " + time.ctime(), "*")
