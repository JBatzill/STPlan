from rest_server import app
from general import config
import general
from database.controller import ctrl_school
from rest_server.rest_db import get_db

#constants
PREFIX = "/school/"

#get all schools
@app.route(PREFIX + "get", subdomain=config.SUBDOMAIN)
def get_schools():
    try:
        res = ctrl_school.get_schools_public(get_db())
    except ValueError as e:
        return general.create_error_message(str(e))

    return general.convert_json(res)

#get school informations
@app.route('/', subdomain="<school_id>." + config.SUBDOMAIN)
def get_school(school_id):
    try:
        _school_id = int(school_id)
        res = ctrl_school.get_school_public(get_db(), _school_id)
    except ValueError as e:
        return general.create_error_message(str(e))

    return general.convert_json(res)
