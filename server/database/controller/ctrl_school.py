import database
from database import sql_commands

#constants
DEFAULT_ID = -1
CREATION_UPDATE_INFO = "Added school to database"

def create_dictionary(_id=DEFAULT_ID, _name="", _shortcut="", _city="", _state="",
                      _country="",_schedule_url="", _username="", _password="", _last_update_info=""):
    return {"_id": _id, "_name": _name, "_shortcut": _shortcut, "_city": _city, "_state": _state, "_country": _country,
            "_schedule_url": _schedule_url, "_username": _username, "_password": _password, "_last_update_info": _last_update_info}

def add_school(db, _name, _shortcut, _url, _city, _username="", _password="", _state="", _country=""):
    if not _name or len(_name) < 2 or len(_name) > 128:
        raise ValueError("Invalid name!")
    if not _shortcut or len(_shortcut) < 2 or len(_shortcut) > 16:
        raise ValueError("Invalid shortcut!")
    if not _url:
        raise ValueError("Invalid url!")
    if not _city or len(_city) < 2 or len(_city) > 32:
        raise ValueError("Invalid city!")

    dic = create_dictionary(_name=_name, _shortcut=_shortcut, _schedule_url=_url, _city=_city,
                            _username=_username, _password=_password, _state=_state, _country=_country,
                            _last_update_info=CREATION_UPDATE_INFO)
    return database.insert_db(db, sql_commands.SQL_SCHOOL_INSERT_ENTRY, dic, True)

def get_schools(db):
    return database.query_db(db, sql_commands.SQL_SCHOOL_READ_ALL)

def get_school(db, _school_id):
    if int(_school_id) < 0:
        raise ValueError("school id must be at least 0!")

    dic = create_dictionary(_id=_school_id)
    return database.query_db(db, sql_commands.SQL_SCHOOL_READ_ID, dic, True)
