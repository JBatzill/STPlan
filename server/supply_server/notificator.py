from datetime import date
from gcm import *
from general import config


#constants

__gcm = GCM(config.GCM_KEY)


def __send_notification(_school_id, _class, data, expire_date):
    topic = __get_topic_name(_school_id, _class)
    time_to_live = __get_time_to_live(expire_date)
    gcm.plaintext_request(registration_id=topic, data=data, time_to_live=time_to_live)


def __get_time_to_live(expire_date):
    expire_date = expire_date.replace(hour=23, minute=59)
    today = date.today()
    return (expire_date - today).total_seconds()


def __get_topic_name(_school_id, _class):
    pass


