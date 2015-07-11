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
#path relative to server\database
SQL_SCHEMA = os.path.join('sql_commands', 'stplan_schema.sql')
DATABASE = 'stplan.db'

#supply server
SUPPLY_UPDATE_INTERVAL = 1*60 #in sec

#logger
LOG_FILE = os.path.join('logs', 'events.log')
LOG_FILE_SIZE = 1024 * 256 #bytes
LOG_HISTORY_SIZE = 10


#GCM
GCM_KEY = 'AIzaSyCSXpMmauRTX6D2Qnmul8CNpkOufrbH8nQ'

#Security
SSL_KEY = os.path.join('rest_server', 'ssl', 'ssl.key')
SSL_CERT = os.path.join('rest_server', 'ssl', 'ssl.cert')
SSL_CERT_DURATION = 10  # in years
SSL_COMPANY = 'Batzill'
SSL_COUNTRY = 'DE'
