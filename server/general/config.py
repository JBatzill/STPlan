import os
# configuration
DEBUG = True

#Rest server
HOST = 'localhost'
PORT = 42142
SERVER_NAME = 'localhost:%s' % PORT
#Rest server.JSON
JSON_ATT_SEPERATOR = ','
JSON_DIC_SEPERATOR = ':'

#Database
#path relative to server\database
SQL_SCHEMA = os.path.join('sql_commands', 'stplan_schema.sql')
DATABASE = 'stplan.db'

#supply server
SUPPLY_UPDATE_INTERVAL = 5*60 #in sec

#logger
LOG_FILE = os.path.join('logs', 'events.log')
LOG_FILE_SIZE = 1024 * 256 #bytes
LOG_HISTORY_SIZE = 10

#Security
SECRET_KEY = 'laerjg67p39awef29gaeratp394zt'
USERNAME = 'jojo'
PASSWORD = 'ironman42'