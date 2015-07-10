from database.controller import ctrl_schedule, ctrl_notification
from logger import get_log_supp

#constants

#data is an instance ParserResult
def process(db, data):
    for res in data:
        try:
            get_log_supp().info("Process school %s, %s:" % (res.get_school_id(), res.get_date()))

            __process_schedule(db, res)
            __process_notifications(db, res)
        except Exception as e:
            get_log_supp().error("Error in data processing for school '%s': %s" % (res.get_school_id(), str(e)))


def __process_schedule(db, data):
    new_schedule = sort_schedule(data.get_schedule())
    old_schedule = sort_schedule(ctrl_schedule.get_schedule_for_date(db, data.get_school_id(), data.get_date()))
    update_list = []
    delete_list = []
    insert_list = []

    n = 0
    o = 0

    while o < len(old_schedule) and n < len(new_schedule):
        o_key = ctrl_schedule.get_unique_real_key(old_schedule[o])
        n_key = ctrl_schedule.get_unique_real_key(new_schedule[n])

        new_schedule[n]["_id"] = old_schedule[o]["_id"]

        if sorted(old_schedule[o].items()) == sorted(new_schedule[n].items()):
            o += 1
            n += 1
            continue
        elif o_key == n_key:
            update_list += [new_schedule[n]]
            o += 1
            n += 1
        elif o_key < n_key:
            delete_list += [old_schedule[o]]
            o += 1
        elif o_key > n_key:
            insert_list += [new_schedule[n]]
            n += 1

    if o < len(old_schedule):
        delete_list += old_schedule[o:]
    elif n < len(new_schedule):
        insert_list += new_schedule[n:]

    ctrl_schedule.insert_schedules(db, insert_list)
    ctrl_schedule.delete_schedules(db, delete_list)
    ctrl_schedule.update_schedules(db, update_list)

    get_log_supp().info("schedule: %s added, %s updated, %s deleted:" % (len(insert_list), len(update_list), len(delete_list)))


def __process_notifications(db, data):
    new_notifications = sort_notifications(data.get_notifications())
    old_notifications = sort_notifications(ctrl_notification.get_notifications_for_date(db, data.get_school_id(), data.get_date()))
    delete_list = []
    insert_list = []

    n = 0
    o = 0

    while o < len(old_notifications) and n < len(new_notifications):
        o_key = ctrl_notification.get_unique_real_key(old_notifications[o])
        n_key = ctrl_notification.get_unique_real_key(new_notifications[n])
        if o_key == n_key:
            o += 1
            n += 1
        elif o_key < n_key:
            delete_list += [old_notifications[o]]
            o += 1
        elif o_key > n_key:
            insert_list += [new_notifications[n]]
            n += 1

    if o < len(old_notifications):
        delete_list += old_notifications[o:]
    elif n < len(new_notifications):
        insert_list += new_notifications[n:]

    ctrl_notification.insert_notifications(db, insert_list)
    ctrl_notification.delete_notifications(db, delete_list)

    get_log_supp().info("notifications: %s added, %s deleted:" % (len(insert_list), len(delete_list)))


def sort_schedule(data):
    return sorted(data, key=ctrl_schedule.get_unique_real_key)

def sort_notifications(data):
    return sorted(data, key=ctrl_notification.get_unique_real_key)
