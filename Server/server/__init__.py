from flask import Flask

#consts
__CONFIGURATION_FILE = "config.py"

app = Flask(__name__)
app.config.from_pyfile(__CONFIGURATION_FILE)
from server import main