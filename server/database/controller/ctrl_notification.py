from datetime import timedelta, date
import database
from database import sql_commands

#constants
__REAL_KEY_SPLITTER = "[#]"
DEFAULT_ID = -1
DEFAULT_DAYS = 365

def create_dictionary(_id=DEFAULT_ID, _school_id="", _date="", _title="", _message=""):
    return {"_id": _id, "_school_id": _school_id, "_date": _date, "_title": _title, "_message": _message}

def get_unique_real_key(dic):
    return str(dic["_school_id"]) + __REAL_KEY_SPLITTER + dic["_date"] + __REAL_KEY_SPLITTER + dic["_title"].lower() + \
           __REAL_KEY_SPLITTER + dic["_message"]

def get_notifications(db, _school_id, _days=DEFAULT_DAYS):
    if int(_school_id) < 0:
        raise ValueError("school id must be at least 0!")
    if _days < 0:
        return ValueError("days must be at least 0!")

    _today = date.today()
    return database.query_db(db, sql_commands.SQL_NOTIFICATION_READ_STD, [_school_id, _today, _today + timedelta(days=_days)])

def get_notifications_for_date(db, _school_id, date):
    if int(_school_id) < 0:
        raise ValueError("school id must be at least 0!")
    return database.query_db(db, sql_commands.SQL_NOTIFICATION_READ_STD, [_school_id, date, date])

def insert_notifications(db, notifications):
    if len(notifications) <= 0:
        return 0
    return database.submit_many_db(db, sql_commands.SQL_NOTIFICATION_INSERT_ENTRY, notifications)

def delete_notifications(db, notifications):
    if len(notifications) <= 0:
        return 0
    return database.submit_many_db(db, sql_commands.SQL_NOTIFICATION_DELETE_ENTRY, notifications)
