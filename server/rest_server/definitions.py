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
