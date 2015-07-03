import sys, os
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(MAIN_DIR, ".."))
#----------------------------------------------------------------------------------------------------------------------


from logger import get_log_db
from database import init_db

get_log_db().info("creating database")

init_db()