from datetime import date
from rest_server import app
from flask import request
from datetime import timedelta
from rest_server.definitions import *
from rest_server.database import query_db
from database.sql_commands import SQL_READ_STD

#get schedule for given school and properties
@app.route('/getschedule', subdomain="<school>." + SUBDOMAIN)
def get_schedule(school):
    try:
        _days = int(request.args.get('days', DEFAULT_DAYS))
        _class = request.args.get('class', DEFAULT_CLASS)
    except ValueError:
        return create_error_message("Unable to convert given parameter!");

    if _days < 0:
        return create_error_message("days must be at least 0!")

    _today = date.today()

    print(str(_today) + "#request: " + school + ", " + str(_days) + ", " + _class)
    res = query_db(SQL_READ_STD, [school, _today, _today + timedelta(days=_days), _class])

    return str(res)
