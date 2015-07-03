from database import connect_db
db = None
#----------------------------------------------------------------------------------

from general.config import SUPPLY_UPDATE_INTERVAL
from supply_server.supplier.supp_wieland_gymnasium import SuppWielandGymnasium
import time, datetime

#list containing all existing suppliers
suppliers = [SuppWielandGymnasium()]

while True:
    db = connect_db()
    for supp in suppliers:
        #time measurement
        t = datetime.datetime.now()

        count = supp.update(db)

        #print little overview
        print("#" + supp.get_name() + "[" + str(int(1000 * (datetime.datetime.now() - t).total_seconds())) + "ms]: " + str(count) + " entries found")

    db.close()

    time.sleep(SUPPLY_UPDATE_INTERVAL)