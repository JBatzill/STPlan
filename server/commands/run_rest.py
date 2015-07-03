#!flask/bin/python
import sys, os
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(MAIN_DIR, ".."))
#----------------------------------------------------------------------------------------------------------------------


from rest_server import app
from general.config import HOST, PORT
from logger import get_log_rest
get_log_rest().info("starting rest server")
app.run(host=HOST, port=PORT)