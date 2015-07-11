import logging
import logging.handlers
import os

from general.config import LOG_FILE, LOG_FILE_SIZE, LOG_HISTORY_SIZE, DEBUG



#constants
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

LOGGER_NAME_MAIN = 'main'
LOGGER_NAME_DB = 'database'
LOGGER_NAME_REST = 'rest_server'
LOGGER_NAME_SUPP = 'supply_server'

# Add the log message handler to the logger
formatter = logging.Formatter('[%(asctime)s] # %(levelname)8s # %(name)13s >  %(message)s')
handler = logging.handlers.RotatingFileHandler(os.path.join(MAIN_DIR, LOG_FILE), maxBytes=LOG_FILE_SIZE, backupCount=LOG_HISTORY_SIZE)
handler.setFormatter(formatter)
consoleHandler = logging.StreamHandler()

___main_logger = logging.getLogger(LOGGER_NAME_MAIN)
___main_logger.setLevel(logging.DEBUG)
___main_logger.addHandler(handler)

___db_logger = logging.getLogger(LOGGER_NAME_DB)
___db_logger.setLevel(logging.INFO)
___db_logger.addHandler(handler)

___rest_logger = logging.getLogger(LOGGER_NAME_REST)
___rest_logger.setLevel(logging.INFO)
___rest_logger.addHandler(handler)

___supp_logger = logging.getLogger(LOGGER_NAME_SUPP)
___supp_logger.setLevel(logging.INFO)
___supp_logger.addHandler(handler)

# write on console too if DEBUG = Tue
if DEBUG:
    ___supp_logger.addHandler(consoleHandler)
    ___rest_logger.addHandler(consoleHandler)
    ___db_logger.addHandler(consoleHandler)
    ___main_logger.addHandler(consoleHandler)

def get_log_main():
    return ___main_logger

def get_log_db():
    return ___db_logger

def get_log_rest():
    return ___rest_logger

def get_log_supp():
    return ___supp_logger
