import json

from general.config import JSON_ATT_SEPERATOR, JSON_DIC_SEPERATOR


#constants for http requests
SUBDOMAIN = "stplan"
DEFAULT_DAYS = 365
DEFAULT_TEACHER = "%"
DEFAULT_SCHOOL = "%"
DEFAULT_CLASS = "%"

#create error message with unique beginning:
ERROR = "Error: "
def create_error_message(msg):
    return ERROR + msg;

#JSON-stuff
def json_dic(dic):
    return json.dumps(dic, sort_keys=True, separators=(JSON_ATT_SEPERATOR, JSON_DIC_SEPERATOR))
