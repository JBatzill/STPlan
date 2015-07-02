import os
import sqlite3
from contextlib import closing
from general import app
from flask import request, session, g


#constants
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
__SQL_SCHEMA = "\stplan_schema.sql"

def connect_db():
    return sqlite3.connect(MAIN_DIR + app.config['DATABASE'])

#create db from sql schema
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource(MAIN_DIR + __SQL_SCHEMA, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

#executed before the db request
@app.before_request
def before_request():
    g.db = connect_db()
    g.db.row_factory = sqlite3.Row

#executed after the response has been created
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#runs the given sql query using the given args.
#if one=True, only the first result will be returned.
def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    res = cur.fetchall()
    cur.close()
    return (res[0] if res else None) if one else res