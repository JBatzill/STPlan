from rest_server import app
from flask import request
import general
from general import config
from database.controller import ctrl_user, ctrl_subscription
from rest_server.rest_db import get_db
from sqlite3 import IntegrityError

#constants
PREFIX = "/subscription/"


@app.route(PREFIX + "add", subdomain="<school_id>." + config.SUBDOMAIN)
def add_subscription(school_id):
    try:
        _uuid = request.args.get('uuid', None)
        _class = request.args.get('class', None)
    except ValueError:
        return general.create_error_message("Unable to convert given parameter!");

    try:
        res1 = ctrl_user.get_user_id_by_uuid(get_db(), _uuid)
        if res1:
            res2 = ctrl_subscription.add_subscription(get_db(), res1['_id'], school_id, _class)
        else:
            return "Wrong uuid"
    except (ValueError, IntegrityError) as e:
        return general.create_error_message(str(e))

    return general.convert_json(res2)


@app.route(PREFIX + "delete", subdomain="<school_id>." + config.SUBDOMAIN)
def delete_subscription(school_id):
    try:
        _uuid = request.args.get('uuid', None)
        _class = request.args.get('class', None)
    except ValueError:
        return general.create_error_message("Unable to convert given parameter!");

    try:
        res1 = ctrl_user.get_user_id_by_uuid(get_db(), _uuid)
        if res1:
            res2 = ctrl_subscription.del_subscription(get_db(), res1['_id'], school_id, _class)
    except ValueError as e:
        return general.create_error_message(str(e))

    return general.convert_json(res2)

@app.route(PREFIX + "get", subdomain=config.SUBDOMAIN)
def get_subscription():
    try:
        _uuid = request.args.get('uuid', None)
    except ValueError:
        return general.create_error_message("Unable to convert given parameter!");

    try:
        res = ctrl_subscription.get_subscriptions_uuid(get_db(), _uuid)
    except ValueError as e:
        return general.create_error_message(str(e))

    return general.convert_json(res)