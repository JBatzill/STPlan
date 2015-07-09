from datetime import timedelta, date
import database
from database import sql_commands

#constants
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

def get_schedules(db, _school_id, _days=DEFAULT_DAYS, _class=DEFAULT_CLASS):
    if _school_id < 0:
        raise ValueError("school id must be at least 0!")
    if _days < 0:
        return ValueError("days must be at least 0!")

    _today = date.today()
    return database.query_db(db, sql_commands.SQL_SCHEDULE_READ_STD, [_school_id, _today, _today + timedelta(days=_days), _class])
