import os
# configuration
DEBUG = True #False

#Rest server
HOST = 'localhost' #'0.0.0.0'
PORT = 42142
SERVER_NAME = 'localhost:%s' % PORT #'batzill.net:%s' % PORT
#Rest server.JSON
JSON_ATT_SEPERATOR = ','
JSON_DIC_SEPERATOR = ':'

#Database
#path relative to server\rest_db
SQL_SCHEMA = os.path.join('sql_commands', 'stplan_schema.sql')
DATABASE = 'stplan.db'

#supply server
SUPPLY_UPDATE_INTERVAL = 1*60 #in sec

#logger
LOG_FILE = os.path.join('logs', 'events.log')
LOG_FILE_SIZE = 1024 * 256 #bytes
LOG_HISTORY_SIZE = 10

#Security
SECRET_KEY = 'laerjg67p39awef29gaeratp394zt'
USERNAME = 'jojo'
PASSWORD = 'ironman42'