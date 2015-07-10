#! /usr/bin/env python
import sys, os
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(MAIN_DIR, ".."))
open(os.path.join(MAIN_DIR, "pids", "run_supply.pid"),"w").write(str(os.getpid()))
#----------------------------------------------------------------------------------------------------------------------


from logger import get_log_supp
from supply_server import run, parser

get_log_supp().info("start supply server")
get_log_supp().info("schools: %s", [x.get_name() for x in parser])
run()