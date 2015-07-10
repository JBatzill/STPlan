import database
from rest_server import app
from flask import g



def get_db():
    return g.db

#executed before the db request
@app.before_request
def before_request():
    g.db = database.connect_db()

#executed after the response has been created
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()