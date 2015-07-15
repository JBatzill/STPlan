#! /usr/bin/env python
import sys, os
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(MAIN_DIR, ".."))
open(os.path.join(MAIN_DIR, "pids" ,"run_rest.pid"),"w").write(str(os.getpid()))
#----------------------------------------------------------------------------------------------------------------------
from logger import get_log_rest
import rest_server


get_log_rest().info("setting up rest server")
rest_server.set_up()
get_log_rest().info("starting rest server")
rest_server.run()
