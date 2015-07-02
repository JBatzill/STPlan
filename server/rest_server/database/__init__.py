import os, database
from rest_server import app
from flask import g

#constants
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))


def query_db(query, args=(), one=False):
    return database.query_db(g.db, query, args, one)

#executed before the db request
@app.before_request
def before_request():
    g.db = database.connect_db()
    #method used to convert a row in a arbitrary object.
    #Used to convert result of db requests
    g.db.row_factory = database.dict_factory

#executed after the response has been created
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()