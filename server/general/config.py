# configuration
DEBUG = True

#Rest server
SERVER_NAME = 'localhost:42142'

#Database
#path relative to server\database
SQL_SCHEMA = '\sql_commands\stplan_schema.sql'
DATABASE = '\stplan.db'

#supply server
SUPPLY_UPDATE_INTERVAL = 60 #in sec

#logger
LOG_FILE = '\logs\events.log'
LOG_FILE_SIZE = 1024 * 256 #bytes
LOG_HISTORY_SIZE = 10

#Security
SECRET_KEY = 'laerjg67p39awef29gaeratp394zt'
USERNAME = 'jojo'
PASSWORD = 'ironman42'