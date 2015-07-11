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
