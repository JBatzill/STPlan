from rest_server import app
from flask import request
from rest_server.constants import *
from rest_server.database import query_db

#get schedule for given school and properties
@app.route('/getschedule', subdomain="<school>." + SUBDOMAIN)
def get_schedule(school):
    try:
        days = int(request.args.get('days', DEFAULT_DAYS))
        teacher = request.args.get('teacher', DEFAULT_TEACHER)
        _class = request.args.get('class', DEFAULT_CLASS)
    except ValueError:
        return create_error_message("Unable to convert given parameter!");
    else:
        print("request: " + school + ", " + str(days) + ", " + teacher + ", " + _class)

    if(days < 0):
        return create_error_message("days must be at least 0!")

    res = query_db("select * from 'schedule'", [])


    return str(res)