import time as t
from datetime import datetime, timedelta
from core import file


# ===== Fonctions =====
def TIME():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def TIMEDIFF(date1, date2):
    fdate1 = t.strptime(date1, "%d/%m/%Y %H:%M:%S")
    fdate2 = t.strptime(date2, "%d/%m/%Y %H:%M:%S")
    if (fdate2.tm_mday >= fdate1.tm_mday+6 or fdate2.tm_mon != fdate1.tm_mon):
        return True
    return False

def DATE():
    return datetime.now().strftime("%Y_%m_%d")


class bcolors:
    end = '\033[0m'
    black = '\033[30m'
    white = '\033[37m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    lightblue = '\033[36m'
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


# ===== Variables =====
DATE = DATE()
DATEnTIME = datetime.now().strftime("%Y%m%d-%H%M")


# ===== Export =====
export_folder = 'export/'
if (not file.exist(export_folder)):
    file.createdir(export_folder)
    

##### Initialisation des constantes #####
CONFIG = file.json_read("config.json")
VERSION = CONFIG['version']
NAME = CONFIG['name']
AUTHOR = CONFIG['author']