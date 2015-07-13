from rest_server import app
from flask import request
import general
from general import config
from database.controller import ctrl_user
from rest_server.rest_db import get_db
from sqlite3 import IntegrityError

#constants
PREFIX = "/user/"


@app.route(PREFIX + "register", subdomain=config.SUBDOMAIN)
def register_device():
    try:
        _uuid = request.args.get('uuid', None)
        _reg_id = request.args.get('reg_id', None)
    except ValueError:
        return general.create_error_message("Unable to convert given parameter!");

    try:
        res = ctrl_user.add_user(get_db(), _uuid, _reg_id)
    except (ValueError, IntegrityError) as e:
        return general.create_error_message(str(e))

    return general.convert_json(res)

@app.route(PREFIX + "unregister", subdomain=config.SUBDOMAIN)
def unregister_device():
    try:
        _uuid = request.args.get('uuid', None)
    except ValueError:
        return general.create_error_message("Unable to convert given parameter!");

    try:
        res = ctrl_user.del_user_uuid(get_db(), _uuid)
    except ValueError as e:
        return general.create_error_message(str(e))

    return general.convert_json(res)

@app.route(PREFIX + "update", subdomain=config.SUBDOMAIN)
def update_device():
    try:
        _uuid = request.args.get('uuid', None)
        _new_reg_id = request.args.get('new_reg_id', None)
    except ValueError:
        return general.create_error_message("Unable to convert given parameter!");

    try:
        res = ctrl_user.update_user_reg_id(get_db(), _uuid, _new_reg_id)
    except (ValueError, IntegrityError) as e:
        return general.create_error_message(str(e))

    return general.convert_json(res)
