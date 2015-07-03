#!flask/bin/python
from rest_server import app
from logger import get_log_rest
get_log_rest().info("starting rest server")
app.run()