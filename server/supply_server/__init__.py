from database import connect_db
db = None
#----------------------------------------------------------------------------------

from general.config import SUPPLY_UPDATE_INTERVAL
from supply_server.supplier.supp_wieland_gymnasium import SuppWielandGymnasium
import time

#list containing all existing suppliers
suppliers = [SuppWielandGymnasium()]

while True:
    db = connect_db()
    for supp in suppliers:
        supp.update()
    db.close()

    time.sleep(SUPPLY_UPDATE_INTERVAL)