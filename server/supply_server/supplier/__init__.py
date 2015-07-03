from database import submit_until_db
from database.sql_commands import SQL_UPDATE_NKEY, SQL_INSERT
from supply_server import db


class BaseSupplier:
    def submit_entry(self, param):
        count = submit_until_db(db, [(SQL_UPDATE_NKEY, param), (SQL_INSERT, param)])
        print(str(count))

    def update(self):
        raise NotImplementedError()
