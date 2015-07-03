from logger import get_log_supp
from supply_server import run, suppliers

get_log_supp().info("start supply server")
get_log_supp().info("schools: %s", [x.get_name() for x in suppliers])
run()