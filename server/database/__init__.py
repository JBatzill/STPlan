import sqlite3
import os
from contextlib import closing
from general.config import DATABASE
from database.sql_commands import SQL_CREATE_DB

#constants
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

def connect_db():
    return sqlite3.connect(MAIN_DIR + DATABASE)

#create db from sql schema
def init_db():
    with closing(connect_db()) as db:
        db.cursor().executescript(SQL_CREATE_DB)
        db.commit()

def dict_factory(cursor, row):
    #enumerate creates (0, ..[0]) -> (1, ..[1]) -> ...
    #description is readonly list containing 7-tuples
    #where only the first item is not NONE but the first word of the name of the ith column
    d = {}
    for (idx, col) in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_dictionary(_school="", _date="", _class="", _time="", _subject="", _teacher="", _new_subject="",\
                      _new_teacher="", _new_room="", _origin="", _treatment="", _reason=""):
    return {"_school": _school, "_date": _date, "_class": _class, "_time": _time,\
            "_subject": _subject, "_teacher": _teacher, "_new_subject": _new_subject,\
            "_new_teacher": _new_teacher, "_new_room": _new_room, "_origin": _origin,\
            "_treatment": _treatment, "_reason": _reason}


#runs the given sql query using the given args.
#if one=True, only the first result will be returned.
def query_db(db, query, args=(), one=False):
    cur = db.execute(query, args)
    res = cur.fetchall()
    cur.close()
    return (res[0] if res else None) if one else res

def submit_db(db, query, args=()):
    cur = db.execute(query, args)
    cur.close()
    db.commit()
    return cur.rowcount

def submit_many_db(db, query, args):
    cur = db.executemany(query, args)
    cur.close()
    db.commit()
    return cur.rowcount

def submit_until_db(db, script):
    cur = db.cursor()
    for (sql, dic) in script:
        cur.execute(sql, dic)
        if cur.rowcount > 0:
            break
    cur.close()
    db.commit()
    return cur.rowcount
