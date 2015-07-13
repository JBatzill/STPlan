from rest_server import app
from flask import request
import general
from general import config
from database.controller import ctrl_schedule
from rest_server.rest_db import get_db

#constants
PREFIX = "/schedule/"


#get schedule for given school and properties
@app.route(PREFIX + "get", subdomain="<school_id>." + config.SUBDOMAIN)
def get_schedule(school_id):
    try:
        _school_id = int(school_id)
        _days = int(request.args.get('days', ctrl_schedule.DEFAULT_DAYS))
        _class = request.args.get('class', ctrl_schedule.DEFAULT_CLASS)
    except ValueError:
        return general.create_error_message("Unable to convert given parameter!");

    try:
        res = ctrl_schedule.get_schedule_for_date(get_db(), _school_id, _days, _class)
    except ValueError as e:
        return general.create_error_message(str(e))

    return general.convert_json(res)