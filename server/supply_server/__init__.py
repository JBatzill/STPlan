import time

from database import connect_db
from general.config import SUPPLY_UPDATE_INTERVAL
from supply_server.parser.parser_wieland_gymnasium import ParserWielandGymnasium
from logger import get_log_supp


#list containing all existing suppliers
suppliers = [ParserWielandGymnasium()]

def run():
    while True:
        db = connect_db()
        for supp in suppliers:
            if supp.check_for_change():
                get_log_supp().info("updates available for '%s'" % (supp.get_name()))
                count = supp.parse(db)
                get_log_supp().info("updated '%s': %s entries found" % (supp.get_name(), str(count)))

        db.close()

        time.sleep(SUPPLY_UPDATE_INTERVAL)