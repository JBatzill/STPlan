from rest_server import app
from flask import request
from rest_server.definitions import *
import general
from database.controller import ctrl_schedule, ctrl_school
from rest_server.rest_db import get_db

#get all schools
@app.route('/getschools', subdomain=SUBDOMAIN)
def get_schools():
    try:
        res = ctrl_school.get_schools(get_db())
    except ValueError as e:
        return general.create_error_message(str(e))

    return general.json_dic(res)

#get schedule for given school and properties
@app.route('/', subdomain="<school_id>." + SUBDOMAIN)
def get_school(school_id):
    try:
        _school_id = int(school_id)
        res = ctrl_school.get_school(get_db(), _school_id)
    except ValueError as e:
        return general.create_error_message(str(e))

    return general.json_dic(res)

#get schedule for given school and properties
@app.route('/getschedule', subdomain="<school_id>." + SUBDOMAIN)
def get_schedule(school_id):
    try:
        _school_id = int(school_id)
        _days = int(request.args.get('days', ctrl_schedule.DEFAULT_DAYS))
        _class = request.args.get('class', ctrl_schedule.DEFAULT_CLASS)
    except ValueError:
        return general.create_error_message("Unable to convert given parameter!");

    try:
        res = ctrl_schedule.get_schedules(get_db, _school_id, _days, _class)
    except ValueError as e:
        return general.create_error_message(str(e))

    return general.json_dic(res)
