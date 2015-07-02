from rest_server import app
from flask import request

#constants for http requests
__SUBDOMAIN = "stplan"
__DEFAULT_DAYS = 0
__DEFAULT_TEACHER = "all"
__DEFAULT_CLASS = "all"

#create error message with unique beginning:
__ERROR = "Error: "
def create_error_message(msg):
    return __ERROR + msg;


#rest_server-stuff

#get schedule for given school and properties
@app.route('/getschedule', subdomain="<school>."+__SUBDOMAIN)
def get_schedule(school):
    try:
        days = int(request.args.get('days', __DEFAULT_DAYS))
        teacher = request.args.get('teacher', __DEFAULT_TEACHER)
        _class = request.args.get('class', __DEFAULT_CLASS)
    except ValueError:
        return create_error_message("Unable to convert given parameter!");
    else:
        print("request: " + school + ", " + str(days) + ", " + teacher + ", " + _class)

    if(days < 0):
        return create_error_message("days must be at least 0!")




    return str(days)