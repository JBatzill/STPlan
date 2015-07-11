import database
from database import sql_commands

#constants
DEFAULT_ID = -1
def create_dictionary(_id=DEFAULT_ID, _user_id="", _school_id="", _class=""):
    return {"_id": _id, "_user_id": _user_id, "_school_id": _school_id, "_class": _class}

def add_subscription(db, _user_id, _school_id, _class):
    if not _user_id:
        raise ValueError("user id must be not null for a valid subscription!")
    if not _school_id:
        raise ValueError("school id must be not null for a valid subscription!")
    if not _class:
        raise ValueError("class must be not null for a valid subscription!")

    dic = create_dictionary(_uuid=_user_id, _reg_id=_school_id, _class=_class)
    return database.insert_db(db, sql_commands.SQL_SUB_INSERT_ENTRY, dic, True)


def del_subscription(db, _user_id, _school_id, _class):
    if not _user_id:
        raise ValueError("user id must be not null for a valid subscription!")
    if not _school_id:
        raise ValueError("school id must be not null for a valid subscription!")
    if not _class:
        raise ValueError("class must be not null for a valid subscription!")

    dic = create_dictionary(_uuid=_user_id, _reg_id=_school_id, _class=_class)
    return database.insert_db(db, sql_commands.SQL_SUB_INSERT_ENTRY, dic, True)
