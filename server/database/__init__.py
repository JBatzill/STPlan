import sqlite3
import os
from contextlib import closing
from general.config import DATABASE, SQL_SCHEMA

#constants
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

def connect_db():
    return sqlite3.connect(MAIN_DIR + DATABASE)

#create db from sql schema
def init_db():
    with closing(connect_db()) as db:
        with open(MAIN_DIR + SQL_SCHEMA, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def dict_factory(cursor, row):
    #enumerate creates (0, ..[0]) -> (1, ..[1]) -> ...
    #description is readonly list containing 7-tuples
    #where only the first item is not NONE but the first word of the name of the ith column
    d = {}
    for (idx, col) in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#runs the given sql query using the given args.
#if one=True, only the first result will be returned.
def query_db(db, query, args=(), one=False):
    cur = db.execute(query, args)
    res = cur.fetchall()
    cur.close()
    return (res[0] if res else None) if one else res