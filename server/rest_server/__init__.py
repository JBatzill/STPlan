import os
from flask import Flask

#constants
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

#consts
__CONFIGURATION_FILE = "\..\general\config.py"

app = Flask(__name__)
app.config.from_pyfile(MAIN_DIR + __CONFIGURATION_FILE)
from rest_server import main