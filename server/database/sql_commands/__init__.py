import os

#constants
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))

def __read_command(file):
    with open(os.path.join(MAIN_DIR, file), mode='r') as f:
        return f.read()

#SQL_COMMANDS
SQL_CREATE_DB = __read_command("stplan_schema.sql")

SQL_SCHEDULE_READ_STD = __read_command("schedule_read_std.sql")
SQL_SCHEDULE_INSERT_ENTRY = __read_command("schedule_insert_entry.sql")
SQL_SCHEDULE_DELETE_ENTRY = __read_command("schedule_delete_entry.sql")
SQL_SCHEDULE_UPDATE_ENTRY = __read_command("schedule_update_entry.sql")

SQL_NOTIFICATION_READ_STD = __read_command("notification_read_std.sql")
SQL_NOTIFICATION_INSERT_ENTRY = __read_command("notification_insert_entry.sql")
SQL_NOTIFICATION_DELETE_ENTRY = __read_command("notification_delete_entry.sql")

SQL_SCHOOL_READ_ALL = __read_command("school_read_all.sql")
SQL_SCHOOL_READ_ID = __read_command("school_read_id.sql")
SQL_SCHOOL_INSERT_ENTRY = __read_command("school_insert_entry.sql")
SQL_SCHOOL_READ_ALL_PUBLIC = __read_command("school_read_all_public.sql")

SQL_USER_INSERT_ENTRY = __read_command("user_insert_entry.sql")