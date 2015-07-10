import time

from database import connect_db
from general.config import SUPPLY_UPDATE_INTERVAL
from supply_server.parser.parser_wieland_gymnasium import ParserWielandGymnasium
from logger import get_log_supp
from supply_server import processor


#list containing all existing suppliers
__db = connect_db()
parser = [ParserWielandGymnasium(__db)]
__db.close()

def run():
    while True:
        db = connect_db()
        for pa in parser:
            if pa.check_for_change():
                get_log_supp().info("updates available for '%s'" % (pa.get_name()))

                try:
                    data = pa.parse(db)
                    processor.process(db, data)
                except Exception as e:
                    get_log_supp().info("error getting data for %s:\n%s" % (pa.get_name(), str(e)))

        db.close()

        time.sleep(SUPPLY_UPDATE_INTERVAL)