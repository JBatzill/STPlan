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

    dic = create_dictionary(_user_id=_user_id, _school_id=_school_id, _class=_class)
    return database.insert_db(db, sql_commands.SQL_SUB_INSERT_ENTRY, dic, True)

def del_subscription(db, _id):
    if int(_id) < 0:
        raise ValueError("subscription id must be not null!")

    dic = create_dictionary(_id=_id)
    db.submit_db(db, sql_commands.SQL_SUB_DELETE_ENTRY_ID, dic)

def del_subscription(db, _user_id, _school_id, _class):
    if not _user_id:
        raise ValueError("user id must be not null for a valid subscription!")
    if not _school_id:
        raise ValueError("school id must be not null for a valid subscription!")
    if not _class:
        raise ValueError("class must be not null for a valid subscription!")

    dic = create_dictionary(_user_id=_user_id, _school_id=_school_id, _class=_class)
    return database.submit_db(db, sql_commands.SQL_SUB_DELETE_ENTRY, dic)

def get_subscriptions_uuid(db, _uuid):
    if not _uuid:
        raise ValueError("uuid must be not null!")

    dic =  {"_uuid": _uuid}
    return database.query_db(db, sql_commands.SQL_SUB_READ_UUID, dic)

def get_subscriptions_school_id(db, _school_id):
    if not _school_id:
        raise ValueError("school id must be not null!")

    dic = create_dictionary(_school_id=_school_id)
    return database.query_db(db, sql_commands.SQL_SUB_READ_SCHOOL, dic)
