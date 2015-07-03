from logger import get_log_db
from database import init_db

get_log_db().info("creating database")

init_db()