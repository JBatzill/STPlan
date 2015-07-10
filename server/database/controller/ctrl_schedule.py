from datetime import timedelta, date
import database
from database import sql_commands

#constants
__REAL_KEY_SPLITTER = "[#]"
DEFAULT_ID = -1
DEFAULT_DAYS = 365
DEFAULT_TEACHER = "%"
DEFAULT_CLASS = "%"

def create_dictionary(_id=DEFAULT_ID, _school_id="", _date="", _class="", _time="", _subject="", _teacher="", _new_subject="",
                      _new_teacher="", _new_room="", _origin="", _treatment="", _note=""):
    return {"_id": _id, "_school_id": _school_id, "_date": _date, "_class": _class, "_time": _time,
            "_subject": _subject, "_teacher": _teacher, "_new_subject": _new_subject,
            "_new_teacher": _new_teacher, "_new_room": _new_room, "_origin": _origin,
            "_treatment": _treatment, "_note": _note}

def get_unique_real_key(dic):
    return str(dic["_school_id"]) + __REAL_KEY_SPLITTER + dic["_date"] + __REAL_KEY_SPLITTER + dic["_class"].lower() + \
           __REAL_KEY_SPLITTER + dic["_time"] + __REAL_KEY_SPLITTER + dic["_teacher"].lower() + __REAL_KEY_SPLITTER + dic["_new_teacher"].lower()

def get_schedule(db, _school_id, _days=DEFAULT_DAYS, _class=DEFAULT_CLASS):
    if int(_school_id) < 0:
        raise ValueError("school id must be at least 0!")
    if _days < 0:
        return ValueError("days must be at least 0!")

    _today = date.today()
    return database.query_db(db, sql_commands.SQL_SCHEDULE_READ_STD, [_school_id, _today, _today + timedelta(days=_days), _class])

def get_schedule_for_date(db, _school_id, date, _class=DEFAULT_CLASS):
    if int(_school_id) < 0:
        raise ValueError("school id must be at least 0!")
    return database.query_db(db, sql_commands.SQL_SCHEDULE_READ_STD, [_school_id, date, date, _class])

def insert_schedules(db, schedules):
    if len(schedules) <= 0:
        return 0
    return database.submit_many_db(db, sql_commands.SQL_SCHEDULE_INSERT_ENTRY, schedules)

def update_schedules(db, schedules):
    if len(schedules) <= 0:
        return 0
    return database.submit_many_db(db, sql_commands.SQL_SCHEDULE_UPDATE_ENTRY, schedules)

def delete_schedules(db, schedules):
    if len(schedules) <= 0:
        return 0
    return database.submit_many_db(db, sql_commands.SQL_SCHEDULE_DELETE_ENTRY, schedules)
