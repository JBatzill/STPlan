from database import connect_db
from general.config import SUPPLY_UPDATE_INTERVAL
from supply_server.supplier.supp_wieland_gymnasium import SuppWielandGymnasium
from logger import get_log_supp
import time, datetime

#list containing all existing suppliers
suppliers = [SuppWielandGymnasium()]

def run():
    while True:
        db = connect_db()
        for supp in suppliers:
            if supp.check_for_change():
                get_log_supp().info("updates available for '%s'" % (supp.get_name()))
                count = supp.update(db)
                get_log_supp().info("updated '%s': %s entries found" % (supp.get_name(), str(count)))

        db.close()

        time.sleep(SUPPLY_UPDATE_INTERVAL)