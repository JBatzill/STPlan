import os
from flask import Flask

#constants
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

#consts
__CONFIGURATION_FILE = os.path.join("..", "general", "config.py")

app = Flask(__name__)
app.config.from_pyfile(os.path.join(MAIN_DIR, __CONFIGURATION_FILE))
from rest_server.pages import page_notification, page_schedule, page_school, page_subscription, page_user
