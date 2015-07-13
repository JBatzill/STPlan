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
SQL_SCHOOL_READ_PUBLIC_ID = __read_command("school_read_public_id.sql")
SQL_SCHOOL_INSERT_ENTRY = __read_command("school_insert_entry.sql")
SQL_SCHOOL_READ_ALL_PUBLIC = __read_command("school_read_all_public.sql")
SQL_SCHOOL_UPDATE_URL = __read_command("school_update_url.sql")
SQL_SCHOOL_DELETE_ID = __read_command("school_delete_id.sql")

SQL_USER_INSERT_ENTRY = __read_command("user_insert_entry.sql")
SQL_USER_DELETE_UUID = __read_command("user_delete_uuid.sql")
SQL_USER_DELETE_REG_ID = __read_command("user_delete_reg_id.sql")
SQL_USER_UPDATE_REG_ID = __read_command("user_update_reg_id.sql")
SQL_USER_READ_ID_BY_UUID = __read_command("user_read_id_by_uuid.sql")

SQL_SUB_INSERT_ENTRY = __read_command("sub_insert_entry.sql")
SQL_SUB_DELETE_ENTRY = __read_command("sub_delete_entry.sql")
SQL_SUB_DELETE_ENTRY_ID = __read_command("sub_delete_entry_id.sql")
SQL_SUB_READ_UUID = __read_command("sub_read_uuid.sql")

