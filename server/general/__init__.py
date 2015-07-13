import json
from general.config import JSON_ATT_SEPERATOR, JSON_DIC_SEPERATOR

__author__ = 'Johannes'

#create error message with unique beginning:
ERROR = "Error: "
def create_error_message(msg):
    return ERROR + msg;

#JSON-stuff
def convert_json(dic):
    return json.dumps(dic, sort_keys=True, separators=(JSON_ATT_SEPERATOR, JSON_DIC_SEPERATOR))



