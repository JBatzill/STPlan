import database
from database import sql_commands

#constants
DEFAULT_ID = -1
def create_dictionary(_id=DEFAULT_ID, _uuid = "", _reg_id = ""):
    return {"_id": _id, "_uuid": _uuid, "_reg_id": _reg_id}

def add_user(db, _uuid, _reg_id):
    if not _uuid:
        raise ValueError("uuid must be not null!")
    if not _reg_id:
        raise ValueError("reg_id must be not null!")

    dic = create_dictionary(_uuid=_uuid, _reg_id=_reg_id)
    return database.insert_db(db, sql_commands.SQL_USER_INSERT_ENTRY, dic, True)

def del_user_uuid(db, _uuid):
    if not _uuid:
        raise ValueError("uuid must be not null!")

    dic = create_dictionary(_uuid=_uuid)
    return database.submit_db(db, sql_commands.SQL_USER_DELETE_UUID, dic)


def del_user_reg_id(db, _reg_id):
    if not _reg_id:
        raise ValueError("reg id must be not null!")

    dic = create_dictionary(_reg_id=_reg_id)
    return database.submit_db(db, sql_commands.SQL_USER_DELETE_REG_ID, dic)

def update_user_reg_id(db, _id, _new_reg_id):
    if not _new_reg_id:
        raise ValueError("reg id must be not null!")

    dic = create_dictionary(_id=_id, _reg_id=_new_reg_id)
    return database.submit_db(db, sql_commands.SQL_USER_UPDATE_REG_ID, dic)

def get_user_id_by_uuid(db, _uuid):
    if not _uuid:
        raise ValueError("uuid must be not null!")

    dic = create_dictionary(_uuid=_uuid)
    return database.query_db(db, sql_commands.SQL_USER_READ_ID_BY_UUID, dic, True)
