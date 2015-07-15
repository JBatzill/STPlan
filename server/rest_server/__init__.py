import os
from flask import Flask
import ssl
from general import config

#constants
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

#consts
__CONFIGURATION_FILE = os.path.join("..", "general", "config.py")
__SSL_KEY = os.path.join('..', config.SSL_KEY)
__SSL_CERT = os.path.join('..', config.SSL_CERT)

context = None
app = None

def set_up():
    global app
    app = Flask(__name__)
    app.config.from_pyfile(os.path.join(MAIN_DIR, __CONFIGURATION_FILE))
    from rest_server.pages import page_notification, page_schedule, page_school, page_subscription, page_user

def run():
    app.run(host=config.HOST, port=config.PORT, ssl_context=(__SSL_CERT, __SSL_KEY))
