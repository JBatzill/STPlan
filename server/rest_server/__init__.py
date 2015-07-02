#constants for http requests
SUBDOMAIN = "stplan"
DEFAULT_DAYS = 0
DEFAULT_TEACHER = "all"
DEFAULT_CLASS = "all"

#create error message with unique beginning:
ERROR = "Error: "
def create_error_message(msg):
    return ERROR + msg;
